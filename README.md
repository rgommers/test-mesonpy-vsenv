# test-mesonpy-vsenv

Test repository for improved MSVC support in meson-python using the `--vsenv` flag.

## Purpose

This repository demonstrates and validates MSVC compiler support in meson-python across different architectures. It uses vendored git submodules of both meson and meson-python to enable testing of modifications needed for better MSVC support, particularly for cross-compilation scenarios.

## Repository Structure

```
test-mesonpy-vsenv/
├── src/
│   └── testpkg/
│       ├── __init__.py      # Python package
│       └── module.c         # Simple C extension with add() function
├── vendor/
│   ├── meson/               # Git submodule: meson build system
│   ├── meson-python/        # Git submodule: meson-python backend
│   └── meson.py             # Wrapper script to use vendored meson
├── .github/
│   └── workflows/
│       └── msvc-build.yml   # CI workflow for MSVC builds
├── meson.build              # Meson build definition
├── pyproject.toml           # Build configuration
└── README.md
```

## Vendored Submodules

This repository vendors both meson and meson-python as git submodules under the `vendor/` directory:

- **vendor/meson**: The Meson build system (https://github.com/mesonbuild/meson)
- **vendor/meson-python**: The meson-python build backend (https://github.com/mesonbuild/meson-python)

The vendored meson is used via the `vendor/meson.py` wrapper script, configured in `pyproject.toml`:

```toml
[tool.meson-python]
meson = 'vendor/meson.py'
```

The vendored meson-python is used via the `backend-path` setting:

```toml
[build-system]
backend-path = ['vendor/meson-python']
```

This setup allows for local modifications to meson and meson-python to improve MSVC support without requiring upstream changes first.

## MSVC Support via --vsenv

The repository uses meson's `--vsenv` flag to automatically detect and set up the Visual Studio environment on Windows. This is configured in `pyproject.toml`:

```toml
[tool.meson-python.args]
setup = ['--vsenv']
```

This approach works on the native architecture of the build machine (e.g., x64 on windows-latest runners).

## Building Locally

### Prerequisites

- Python 3.9 or later
- Git (for cloning with submodules)
- On Windows: Visual Studio with C++ build tools

### Clone and Build

```bash
# Clone with submodules
git clone --recursive <repository-url>
cd test-mesonpy-vsenv

# Install build dependencies
pip install build ninja

# Build the package
python -m build --wheel

# Install the built package
pip install dist/*.whl

# Test the C extension
python -c "import testpkg; print(testpkg.add(5, 3))"
```

## CI/CD Setup

The repository includes a GitHub Actions workflow (`.github/workflows/msvc-build.yml`) that:

1. Checks out the repository with submodules
2. Sets up Python 3.11
3. Installs ninja and build dependencies
4. Builds the wheel using `python -m build`
5. Installs and tests the built package
6. Uploads the wheel as an artifact

### Current Architecture Support

- **x64**: Native builds on `windows-latest` runners ✅
- **x86**: Planned - requires vendored meson/meson-python modifications for cross-compilation
- **arm64**: Planned - awaiting native `windows-arm64` runners or cross-compilation support

## Future Work

The vendored meson and meson-python submodules will be modified to support:

- Cross-compilation from x64 to x86 on `windows-latest` runners
- Cross-compilation to arm64 when runners become available
- Enhanced MSVC architecture detection and configuration

## Test Package

The `testpkg` package contains a minimal C extension module with a single `add(a, b)` function that returns the sum of two integers. This validates that:

- The C compiler (MSVC) is correctly detected and configured
- C extensions can be built successfully
- The resulting extension module can be imported and used

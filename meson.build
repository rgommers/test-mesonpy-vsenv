project('testpkg', 'c', version: '0.1.0')

py = import('python').find_installation(pure: false)

py.extension_module(
  'module',
  'testpkg/module.c',
  install: true,
  subdir: 'testpkg',
)

py.install_sources(
  'testpkg/__init__.py',
  subdir: 'testpkg',
)

"""Tests for the testpkg C extension module."""

import testpkg


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    result = testpkg.add(5, 3)
    assert result == 8


def test_add_negative_numbers():
    """Test adding two negative numbers."""
    result = testpkg.add(-5, -3)
    assert result == -8


def test_add_mixed_numbers():
    """Test adding positive and negative numbers."""
    result = testpkg.add(10, -3)
    assert result == 7


def test_add_zero():
    """Test adding with zero."""
    result = testpkg.add(0, 5)
    assert result == 5
    
    result = testpkg.add(5, 0)
    assert result == 5

"""Tests of 0x.order_utils.asset_data_utils."""

import pytest

from zero_ex.order_utils.asset_data_utils import (
    encode_erc20_asset_data,
    decode_erc20_asset_data,
    ERC20_ASSET_DATA_BYTE_LENGTH,
)


def test_encode_erc20_asset_data_type_error():
    """Test that passing in a non-string raises a TypeError."""
    with pytest.raises(TypeError):
        encode_erc20_asset_data(123)


def test_decode_erc20_asset_data_type_error():
    """Test that passing in a non-string raises a TypeError."""
    with pytest.raises(TypeError):
        decode_erc20_asset_data(123)


def test_decode_erc20_asset_data_too_short():
    """Test that passing an insufficiently long string raises a ValueError."""
    with pytest.raises(ValueError):
        decode_erc20_asset_data(" " * (ERC20_ASSET_DATA_BYTE_LENGTH - 1))


def test_decode_erc20_asset_data_invalid_proxy_id():
    """Test that passing data with an invalid proxy ID raises a ValueError."""
    with pytest.raises(ValueError):
        decode_erc20_asset_data(
            "0xffffffff" + (" " * ERC20_ASSET_DATA_BYTE_LENGTH)
        )

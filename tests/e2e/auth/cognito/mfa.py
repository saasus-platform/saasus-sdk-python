"""
MFA (Multi-Factor Authentication) utilities

TOTP (Time-based One-Time Password) 生成機能を提供します。
"""

import pyotp


def generate_totp(secret: str) -> str:
    """TOTPコードを生成
    
    Args:
        secret: シークレットコード（Base32エンコード）
        
    Returns:
        6桁のTOTPコード
        
    Example:
        >>> secret = "JBSWY3DPEHPK3PXP"
        >>> code = generate_totp(secret)
        >>> assert len(code) == 6
        >>> assert code.isdigit()
    """
    totp = pyotp.TOTP(secret)
    return totp.now()


def verify_totp(secret: str, code: str) -> bool:
    """TOTPコードを検証
    
    Args:
        secret: シークレットコード（Base32エンコード）
        code: 検証するTOTPコード
        
    Returns:
        検証結果
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

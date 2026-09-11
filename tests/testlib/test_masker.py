"""Maskerクラスの動作検証テスト"""

from tests.testlib.snapshot.masker import Masker


def test_masker_basic():
    """基本的なマスキング機能のテスト"""
    masker = Masker()
    
    # テストデータ
    data = {
        "user_id": "12345",
        "email": "test@example.com",
        "api_key": "secret_key_12345",
        "password": "my_password",
        "token": "bearer_token_xyz"
    }
    
    # マスキング実行
    masked_data = masker.mask(data)
    
    # 検証
    assert masked_data["user_id"] == "12345"  # マスキング対象外
    assert masked_data["email"] == "test@example.com"  # マスキング対象外
    assert masked_data["api_key"] == "***MASKED***"  # マスキング対象
    assert masked_data["password"] == "***MASKED***"  # マスキング対象
    assert masked_data["token"] == "***MASKED***"  # マスキング対象
    
    # マスキング数の確認
    assert masker.get_masked_count() == 3
    
    print("✓ 基本的なマスキング機能が正常に動作しています")


def test_masker_nested():
    """ネストされたオブジェクトのマスキングテスト"""
    masker = Masker()
    
    # ネストされたテストデータ
    data = {
        "user": {
            "id": "12345",
            "credentials": {
                "api_key": "secret_key",
                "secret": "my_secret"
            }
        },
        "settings": {
            "public_key": "public_123",
            "private_key": "private_456"
        }
    }
    
    # マスキング実行
    masked_data = masker.mask(data)
    
    # 検証
    assert masked_data["user"]["id"] == "12345"
    assert masked_data["user"]["credentials"]["api_key"] == "***MASKED***"
    assert masked_data["user"]["credentials"]["secret"] == "***MASKED***"
    assert masked_data["settings"]["public_key"] == "public_123"
    assert masked_data["settings"]["private_key"] == "***MASKED***"
    
    # マスキング数の確認
    assert masker.get_masked_count() == 3
    
    print("✓ ネストされたオブジェクトのマスキングが正常に動作しています")


def test_masker_list():
    """リスト内のマスキングテスト"""
    masker = Masker()
    
    # リストを含むテストデータ
    data = {
        "users": [
            {"id": "1", "api_key": "key1"},
            {"id": "2", "password": "pass2"},
            {"id": "3", "token": "token3"}
        ]
    }
    
    # マスキング実行
    masked_data = masker.mask(data)
    
    # 検証
    assert masked_data["users"][0]["id"] == "1"
    assert masked_data["users"][0]["api_key"] == "***MASKED***"
    assert masked_data["users"][1]["password"] == "***MASKED***"
    assert masked_data["users"][2]["token"] == "***MASKED***"
    
    # マスキング数の確認
    assert masker.get_masked_count() == 3
    
    print("✓ リスト内のマスキングが正常に動作しています")


def test_masker_custom_pattern():
    """カスタムパターンのテスト"""
    masker = Masker(custom_patterns=[r"ssn", r"credit_card"])
    
    # カスタムパターンを含むテストデータ
    data = {
        "name": "John Doe",
        "ssn": "123-45-6789",
        "credit_card": "1234-5678-9012-3456",
        "email": "john@example.com"
    }
    
    # マスキング実行
    masked_data = masker.mask(data)
    
    # 検証
    assert masked_data["name"] == "John Doe"
    assert masked_data["ssn"] == "***MASKED***"
    assert masked_data["credit_card"] == "***MASKED***"
    assert masked_data["email"] == "john@example.com"
    
    # マスキング数の確認
    assert masker.get_masked_count() == 2
    
    print("✓ カスタムパターンのマスキングが正常に動作しています")


def test_masker_case_insensitive():
    """大文字小文字を区別しないマスキングのテスト"""
    masker = Masker()
    
    # 大文字小文字が混在するテストデータ
    data = {
        "API_KEY": "key1",
        "Api_Key": "key2",
        "api_key": "key3",
        "PASSWORD": "pass1",
        "Password": "pass2"
    }
    
    # マスキング実行
    masked_data = masker.mask(data)
    
    # 検証（すべてマスキングされるべき）
    assert masked_data["API_KEY"] == "***MASKED***"
    assert masked_data["Api_Key"] == "***MASKED***"
    assert masked_data["api_key"] == "***MASKED***"
    assert masked_data["PASSWORD"] == "***MASKED***"
    assert masked_data["Password"] == "***MASKED***"
    
    # マスキング数の確認
    assert masker.get_masked_count() == 5
    
    print("✓ 大文字小文字を区別しないマスキングが正常に動作しています")


if __name__ == "__main__":
    test_masker_basic()
    test_masker_nested()
    test_masker_list()
    test_masker_custom_pattern()
    test_masker_case_insensitive()
    print("\n✅ すべてのテストが成功しました！")

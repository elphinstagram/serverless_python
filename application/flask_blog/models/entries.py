# モデル作成時刻セット
from datetime import datetime

# Pynamodb 必要なライブラリ(UTCDateTimeAttributeでエラー…)
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import UTCDateTimeAttribute

# モデル


class Entry(Model):
    class Meta:
        table_name = "serverless_blog_entries"
        region = 'ap-northeast-1'
        aws_access_key_id = 'AWS_ACEESS_KEY_ID'
        aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY'
        host = "http://localhost:8000"
        id = NumberAttribute(hash_key=True, null=False)
        title = UnicodeAttribute(null=True)
        text = UnicodeAttribute(null=True)
        created_at = UTCDateTimeAttribute(default=datetime.now)

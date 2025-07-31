import enum
from pathlib import Path
from typing import Optional, List

from appodus_utils.config.settings import AppodusBaseSettings

class IntegratedPlatform(str, enum.Enum):
    ZOHO_DOC_SIGN = "zoho_doc_sign"
    GOOGLE_DRIVE = "google_drive"
    FLUTTERWAVE = "flutterwave"
    PAYSTACK = "paystack"


class PaymentMethod(str, enum.Enum):
    FLUTTERWAVE = "flutterwave"
    PAYSTACK = "paystack"
    STRIPE = "stripe"


class Settings(AppodusBaseSettings):
    BASE_DIR: str = str(Path(__file__).parent.parent)  # Used by templating engine
    ENABLE_OUT_MESSAGING: bool = False

    # AUTH
    AUTH_URL_PATH: str = "/auths"
    # SOCIAL LOGIN
    SOCIAL_LOGIN_CALLBACK_PATH: Optional[str] = "/socials"
    # GOOGLE
    GOOGLE_AUTH_BASE_URL: str = "https://accounts.google.com/o/oauth2/v2/auth"
    GOOGLE_CLIENT_ID: Optional[str]
    GOOGLE_CLIENT_SECRET: Optional[str]
    # FACEBOOK
    FACEBOOK_AUTH_BASE_URL: str = "https://www.facebook.com/v22.0/dialog/oauth"
    FACEBOOK_APP_ID: Optional[str]
    FACEBOOK_APP_SECRET: Optional[str]
    # APPLE
    APPLE_AUTH_BASE_URL: str = "https://accounts.google.com/o/oauth2/v2/auth"
    APPLE_TEAM_ID: Optional[str]
    APPLE_CLIENT_ID: Optional[str]
    APPLE_KEY_ID: Optional[str]
    APPLE_PRIVATE_KEY: Optional[str]

    # SMS Providers
    SMS_SENDER_ID: Optional[str] = "veriprops"
    SMS_TTL = 25000

    # AUTHJWT
    AUTHJWT_SECRET_KEY: str = "auth_jwt_s3cr3t"
    # Configure application to store and get JWT from cookies
    AUTHJWT_TOKEN_LOCATION: List[str] = ["cookies"]
    # Only allow JWT cookies to be sent over https
    AUTHJWT_COOKIE_SECURE: bool = True
    # Enable csrf double submit protection. default is True
    AUTHJWT_COOKIE_CSRF_PROTECT: bool = True
    # Change to 'lax' in production to make your website more secure from CSRF Attacks, default is None
    AUTHJWT_COOKIE_SAMESITE: str = 'none' # Must be 'none' when AUTHJWT_COOKIE_SECURE = True
    # AUTHJWT_ACCESS_COOKIE_KEY: str = 'Host-access_token'
    # AUTHJWT_REFRESH_COOKIE_KEY: str = 'Host-refresh_token'
    # AUTHJWT_ALGORITHM: str = ""

    # CORS
    ALLOWED_ORIGINS: Optional[str] = """
    http://192.168.0.107:3000,
    http://localhost/,
    http://localhost:3000/,
    http://127.0.0.1/,
    http://127.0.0.1:3000/,
    https://.*\\.vercel\\.app,
    http(s)?://(.+\\.)?vercel\\.app(:\\d{1,5})?$,
    https://appodus-web.vercel.app,
    https://appodus-web-dev.vercel.app,
    https://veriprops-web-staging.vercel.app,
    """

    # TOKEN
    OTP_TOKEN_EXPIRE_SECONDS: Optional[int] = 60 * 5 # 5 mins
    EMAIL_OTP_TOKEN_EXPIRE_SECONDS: Optional[int] = 60 * 30 # 30 mins
    ACCESS_TOKEN_EXPIRE_SECONDS: Optional[int] = 60 * 60 * 24 * 8
    REFRESH_TOKEN_EXPIRE_SECONDS: Optional[int] = 60 * 60 * 24 * 8

    # PAYMENT
    PAYMENT_REDIRECT_URL: str = "https://www.veriprops.properties"
    # FLUTTERWAVE
    FLUTTERWAVE_PUBLIC_KEY: Optional[str] = "random"
    FLUTTERWAVE_SECRET_KEY: Optional[str] = "random"
    FLUTTERWAVE_WEBHOOK_SECRET: Optional[str]  # For verifying webhooks
    FLUTTERWAVE_BASE_URL: Optional[str] = "https://api.flutterwave.com/v3"
    # PAYSTACK
    PAYSTACK_PUBLIC_KEY: Optional[str] = "random"
    PAYSTACK_SECRET_KEY: Optional[str] = "random"
    PAYSTACK_WEBHOOK_SECRET: Optional[str]  # For verifying webhooks
    PAYSTACK_BASE_URL: Optional[str] = "https://api.flutterwave.com/v3"

    # ACTIVES
    ACTIVE_PAYMENT_METHOD: PaymentMethod = PaymentMethod.FLUTTERWAVE

    # TEMPLATING
    TEMPLATE_ENGINE: Optional[str] = "jinja2"


settings = Settings()
settings.set_env_vars() # Set the env vars in os.environ

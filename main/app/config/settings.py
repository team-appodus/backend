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
    # AUTH
    SOCIAL_LOGIN_SUCCESS_PATH: Optional[str] = "/dashboard"
    SOCIAL_SIGNUP_SUCCESS_PATH: Optional[str] = "/start-your-build"

    # CORS
    ALLOWED_ORIGINS: Optional[str] = """
    http://192.168.0.107,
    http://192.168.0.107:3000,
    http://localhost,
    http://localhost:3000,
    http://127.0.0.1,
    http://127.0.0.1:3000,
    http://0.0.0.0:3000,
    https://appodus.com,
    https://www.appodus.com,
    https://staging.appodus.com,
    https://dev.appodus.com,
    https://test.appodus.com,
    https://*.appodus.com,
    """

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

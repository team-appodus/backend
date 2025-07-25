import enum
import os
from pathlib import Path
from typing import Optional, Any, Dict, List

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings, validator, PostgresDsn, AnyUrl


def get_absolute_path(path: str):
    directory = os.getcwd()
    test = 'test'
    main = 'main'
    if test in directory:
        directory = directory.split(sep=test)[0]
    if main in directory:
        directory = directory.split(sep=main)[0]
    directory = os.path.join(directory, path)

    return directory


class SupportedDB(str, enum.Enum):
    MYSQL = 'MYSQL'
    MSSQL = 'MSSQL'
    POSTGRES = 'POSTGRES'
    ORACLE = 'ORACLE'


class FileStorage(str, enum.Enum):
    FILE_SYSTEM = 'FILE_SYSTEM'
    S3 = 'S3'


class IntegratedPlatform(str, enum.Enum):
    ZOHO_DOC_SIGN = "zoho_doc_sign"
    GOOGLE_DRIVE = "google_drive"
    FLUTTERWAVE = "flutterwave"
    PAYSTACK = "paystack"


class PaymentMethod(str, enum.Enum):
    FLUTTERWAVE = "flutterwave"
    PAYSTACK = "paystack"
    STRIPE = "stripe"


class EscrowMethod(str, enum.Enum):
    FLUTTERWAVE = "flutterwave"
    PAYSTACK = "paystack"


class Settings(BaseSettings):
    APP_NAME: str = "veriprops waitlist"
    APP_DOMAIN: str = "http://localhost:8000"
    SHOW_API: bool = True
    ENABLE_OUT_MESSAGING: bool = False

    BASE_DIR: str = str(Path(__file__).parent.parent)
    File_STORAGE: FileStorage = FileStorage.S3

    # Enable / Disable Services
    DISABLE_RATE_LIMITING: bool = False

    # LOGGING
    LOG_LEVEL: Optional[str] = 'DEBUG'
    LOGGER_FILE: Optional[str] = 'logs/logs.txt'
    LOGGER_FILE_PATH: Optional[str] = 'logs'

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

    # TWILIO
    TWILIO_ACCOUNT_SID: Optional[str] = ""
    TWILIO_AUTH_TOKEN: Optional[str] = ""
    TWILIO_PHONE_NUMBER: Optional[str] = ""
    # TERMII
    TERMII_API: Optional[str] = 'https://api.ng.termii.com/api'
    TERMII_API_KEY: Optional[str] = 'TL2bCMPbPo55fYGMiFpA0EyBm3oJ998PY88zXjSzPWV07Ht7oPIouZVX1v7oYJ'
    TERMII_API_SECRET_KEY: Optional[str] = 'tsk_zgeb640a2b0320c09048483cpx'

    # Email Providers
    EMAIL_FROM_ADDRESS: Optional[str] = "noreply@example.com"
    EMAIL_FROM_NAME: str = "veriprops"
    EMAIL_SUBJECTS: Dict[str, str] = {
        "2fa_subject": "Extra Security: Your 2FA Code Inside",
        "account_activation_subject": "Important: Your Account Status",
        "account_deactivation_subject": "Important: Your Account Status",
        "agent_performance_summary_subject": "Your Monthly Performance Report 📈",
        "buyer_canceled_visit_subject": "Showing Cancellation Notice",
        "buyer_referral_incentive_subject": "Earn $500 for Referring Friends!",
        "buyer_scheduled_visit_subject": "Showing Scheduled for Your Property",
        "buyer_tips_content_subject": "Pro Tips to Win in Today's Market",
        "buyer_tour_reminder_subject": "Reminder: Your Tour Is Tomorrow!",
        "counter_offer_received_subject": "New Counter-Offer Waiting for You",
        "email_verification_subject": "One Quick Step: Verify Your Email",
        "escrow_initiated_subject": "Escrow Initiated: Action May Be Needed",
        "escrow_status_update_subject": "Escrow Update: Action May Be Needed",
        "feedback_request_post_transaction_subject": "How Did We Do? Share Your Thoughts",
        "fraud_warning_alert_subject": "Important Security Notice",
        "holiday_festive_greeting_subject": "Season's Greetings from Our Team",
        "id_document_rejected_accepted_subject": "Verification Status Update",
        "id_document_verification_pending_subject": "Complete Your Verification",
        "inactive_user_reengagement_subject": "We Miss You! Check These New Listings",
        "inquiry_confirmation_subject": "We've Received Your Inquiry",
        "invite_test_new_feature_subject": "Exclusive: Test Our New Feature",
        "limited_time_promo_discount_subject": "Last Chance! Special Offer Ending Soon",
        "listing_pending_moderation_subject": "Your Listing Is Being Reviewed",
        "listing_performance_summary_subject": "Your Listing Performance Report 📊",
        "login_diff_device_security_alert_subject": "New Login Detected - Was This You?",
        "name_update_success_subject": "Your Name Has Been Updated ✅",
        "new_agent_welcome_subject": "Power Up Your Real Estate Business! 🚀",
        "new_buyer_lead_alert_subject": "New Buyer Interested in Your Listing!",
        "new_buyer_welcome_subject": "Let's Find Your Dream Home! 🔑",
        "new_feature_announcement_subject": "Exciting New Features Just Launched!",
        "new_message_from_seller_agent_subject": "New Message About Your Property",
        "new_property_match_saved_search_subject": "🔥 Hot Property Alert! Just Listed",
        "new_review_for_agent_subject": "You've Got a New Review!",
        "new_user_email_verification_subject": "One Quick Step: Verify Your Email",
        "new_user_welcome_subject": "Welcome to Your Real Estate Journey! 🏡",
        "offer_accepted_subject": "Congratulations! Offer Accepted 🎉",
        "offer_received_to_seller_subject": "Exciting News! You Have an Offer",
        "offer_rejected_subject": "Update on Your Recent Offer",
        "offer_submitted_confirmation_subject": "Your Offer Has Been Submitted",
        "password_reset_request_subject": "Reset Your Password - Quick & Easy",
        "password_update_success_subject": "Your Password Has Been Updated ✅",
        "phone_verification_subject": "Verify Your Phone - Stay Secure",
        "post_sale_buyer_feedback_request_subject": "How Was Your Home Buying Experience?",
        "post_sale_seller_feedback_request_subject": "Help Us Improve - Quick Survey",
        "price_drop_saved_property_subject": "Price Drop! Your Favorite Just Got Cheaper",
        "price_suggestion_trends_subject": "Smart Pricing Tips for Your Property",
        "property_listed_success_subject": "Congratulations! Your Property Is Live 🎉",
        "property_listing_completion_reminder_subject": "Don't Be John, Complete Your Listing!",
        "property_rejected_with_reasons_subject": "Action Needed: Listing Requires Updates",
        "referral_program_invitation_subject": "You're Invited to Our Referral Program",
        "schedule_tour_confirmation_subject": "Tour Confirmed! See You Soon",
        "seller_referral_incentive_subject": "Refer & Earn - Special Bonus Inside",
        "seller_replied_to_inquiry_subject": "You've Got a Response!",
        "seller_tips_content_subject": "Pro Tips to Win in Today's Market",
        "survey_product_improvement_subject": "Help Us Build a Better Platform",
        "terms_policy_updates_subject": "We've Updated Our Policies",
        "tour_rescheduled_cancelled_subject": "Tour Update: Schedule Change",
        "transaction_completed_subject": "Deal Closed! Transaction Complete ✅",
        "transaction_failed_declined_subject": "Important Transaction Update",
    }

    # SENDGRID
    SENDGRID_API_KEY: Optional[str] = ""
    SENDGRID_API_SECRET: Optional[str] = ""
    # MAILJET
    MAILJET_API_KEY: Optional[str] = 'ded977ed9f458adb55e6f598a0eaee4f'
    MAILJET_API_SECRET: Optional[str] = '449e0d723e92f5399ad2769f33803be6'

    # MESSAGING
    MESSAGING_HEADERS: List[str] = []
    MESSAGING_PRIORITY: int = 2
    MESSAGING_SANDBOX_MODE: bool = False
    MESSAGING_CATEGORIES: List[str] = []
    # messaging_config: Dict[str, str] = {
    #     "from_email": "info@veriprops.com",
    #     "from_name": "veriprops",
    #     "ttl": 3600,
    #     "sms_sender_id": "veriprops",
    #     "headers": [],
    #     "priority": "NORMAL",
    #     "sandbox_mode": False,
    #     "categories": [],
    # }

    # WhatsApp Providers
    WHATSAPP_PHONE_NUMBER_ID: Optional[str] = ""
    WHATSAPP_API: Optional[str] = "https://graph.facebook.com/v22.0"
    # WHATSAPP BUSINESS
    WHATSAPP_BUSINESS_ACCOUNT_ID: Optional[str] = ""
    WHATSAPP_BUSINESS_ACCESS_TOKEN: Optional[str] = ""
    WHATSAPP_BUSINESS_WEBHOOK_VERIFY_TOKEN: Optional[str] = ""

    # PUSH Providers
    # Firebase
    FIREBASE_CREDENTIALS_PATH: Optional[str] = get_absolute_path("service_accounts/firebase-service-account.json")
    # Web Push Configuration
    WEB_PUSH_PRIVATE_KEY: Optional[str]
    WEB_PUSH_PUBLIC_KEY: Optional[str]
    WEB_PUSH_CONTACT_EMAIL: Optional[str] = "notifications@example.com"
    WEB_PUSH_SUBJECT_EMAIL: Optional[str] = "notifications@example.com"

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


    # AWS
    AWS_ACCESS_KEY: Optional[str] = "AKIARSU7K5ZHU4J7VY5F"
    AWS_SECRET_ACCESS_KEY: Optional[str] = "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"
    AWS_S3_PROPERTY_BUCKET: Optional[str] = "veriprops"
    AWS_REGION_NAME: Optional[str] = "us-east-1"
    AWS_S3_PLATFORM_NAME: Optional[str] = FileStorage.S3

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

    # WEBHOOK
    WEBHOOK_PATH: Optional[str] = "/webhooks"

    # ZOHO
    ZOHO_CLIENT_ID: Optional[str]
    ZOHO_CLIENT_SECRET: Optional[str]
    ZOHO_REFRESH_TOKEN: Optional[str]
    ZOHO_DOC_SIGN_DATA_CENTER: Optional[str] = "https://sign.zoho.com"
    ZOHO_WEBHOOK_SECRET: Optional[str]

    # GOOGLE DRIVE
    GOOGLE_WEBHOOK_SECRET: Optional[str]
    GOOGLE_WEBHOOK_NOTIFICATION_TTL: int = 60 * 60 * 24 # 1 Day
    GOOGLE_DOC_CHANGE_UPDATE_WINDOW: int = 60 * 60 * 24 # 1 Day
    GOOGLE_SERVICE_ACCOUNT_FILE: Optional[str] = get_absolute_path("service_accounts/contracts-service_account.json")
    GOOGLE_DOC_PARENT_CONTRACT_ID: str = "1he8Q3Sxs2PSdfoWflNFwlk10MXI7M03QqGW3GdPHuWM"
    GOOGLE_DOC_PARENT_CONTRACT_FOLDER_ID: str = "1lODSM6OMBX4Qan7SPFzJf_zJF6fH9mCA"
    GOOGLE_DOC_PROPERTY_CONTRACT_FOLDER_ID: str = "1VblZfpRnHmQj8DN5nOJNc4C1xbQe9u-h"

    # ACTIVES
    ACTIVE_DOCUMENT_SIGN_PLATFORM: IntegratedPlatform = IntegratedPlatform.ZOHO_DOC_SIGN
    ACTIVE_DOCUMENT_STORAGE_PROVIDER: Optional[str] = FileStorage.S3
    ACTIVE_PAYMENT_METHOD: PaymentMethod = PaymentMethod.FLUTTERWAVE
    ACTIVE_ESCROW_METHOD: EscrowMethod = EscrowMethod.FLUTTERWAVE

    # TEMPLATING
    TEMPLATE_ENGINE: Optional[str] = "jinja2"

    # REDIS
    REDIS_ENABLED: Optional[bool] = False
    REDIS_HOST: Optional[str]
    REDIS_PORT: Optional[str]
    REDIS_USERNAME: Optional[str] = None
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: Optional[str] = '0'
    REDIS_THREAD_SLEEP_TIME: Optional[float] = 0.01

    # DB
    ACTIVE_DB: Optional[SupportedDB] = SupportedDB.POSTGRES
    DB_SCHEME: Optional[str]
    DB_SERVER: Optional[str] = "sqlite:///"
    DB_USER: Optional[str]
    DB_PASSWORD: Optional[str]
    DB_PORT: Optional[str]
    DB_NAME: Optional[str]
    DB_ADDITIONAL_CONFIG: Optional[str]
    SQLALCHEMY_DATABASE_URI: Any
    DB_ENABLE_LOGS: Optional[bool] = True
    DB_ENABLE_LOG_POOL: Optional[bool] = True
    DB_MAIN_THREAD_CONTEXT_ID: int = 12345

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        db_url = v
        if isinstance(v, str):
            return v

        if SupportedDB.POSTGRES == values.get("ACTIVE_DB"):
            db_url = PostgresDsn.build(
                scheme=values.get("DB_SCHEME"),
                user=values.get("DB_USER"),
                password=values.get("DB_PASSWORD"),
                host=values.get("DB_SERVER"),
                port=values.get("DB_PORT"),
                path=f"/{values.get('DB_NAME') or ''}?{values.get('DB_ADDITIONAL_CONFIG')}",
            )
        elif SupportedDB.MYSQL == values.get("ACTIVE_DB"):
            db_url = AnyUrl.build(
                scheme=values.get("DB_SCHEME"),
                user=values.get("DB_USER"),
                password=values.get("DB_PASSWORD"),
                host=values.get("DB_SERVER"),
                port=values.get("DB_PORT"),
                path=f"/{values.get('DB_NAME') or ''}?{values.get('DB_ADDITIONAL_CONFIG')}",
            )
        else:
            db_path = get_absolute_path(os.path.join("main", "app", "db"))
            db = os.path.join(db_path, values.get('DB_NAME'))
            db_url = f"{values.get('DB_SERVER')}{db}?{values.get('DB_ADDITIONAL_CONFIG')}"

            print('db_url: ', db_url)

        return db_url

    class Config:
        env_file = get_absolute_path(f'.env.{os.getenv("appodus_active_env", "local")}')

        load_dotenv(dotenv_path=env_file)
        print(f'env_file: {env_file}')
        env_file_encoding = "utf-8"
        case_sensitive = False

    def set_env_vars(self):
        """Set all settings as environment variables."""
        for key, value in self.dict().items():
            os.environ[key.upper()] = str(value)


settings = Settings()
settings.set_env_vars() # Set the env vars in os.environ

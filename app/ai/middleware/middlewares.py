from app.ai.middleware.emailblocker import email_blocker
from app.ai.middleware.cardblocker import creditcard_blocker

middlewares = [email_blocker, creditcard_blocker]
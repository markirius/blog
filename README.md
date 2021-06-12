# blog

A blog example with admin access use for estudy purpose.

features:

- Django 3
- Class Based View
- Admin management
- Python decouple


* generate .env file with:
`python contrib/make_env.py`

* work with postgres or sqlite


* .env file

|VAR|VALUE|TYPE|
|---|-----|----|
|SECRET_KEY|examplejbb+VirRuW3uYi6wFVe1w39OBmL3xb3Q=example|STRING
|DEBUG|TRUE|BOOLEAN|
|DEVELOPMENT|TRUE|BOOLEAN|
|EMAIL_HOST|smtp.domain.com|STRING|
|EMAIL_HOST_USER|email@domain.com|STRING|
|EMAIL_HOST_PASSWORD|password|STRING|
|EMAIL_PORT|587|INT|
|EMAIL_USE_TLS|TRUE|BOOLEAN|
|LANGUAGE_CODE|pt-br|STRING|
|DATABASE_URL|postgres://username:password@address:port/database|STRING|
|ALLOWED_HOSTS|localhost, 0.0.0.0, 127.0.0.1|STRING|
|TIME_ZONE|UTC|STRING|
|USE_I18N|TRUE|BOOLEAN|
|USE_L10N|TRUE|BOOLEAN|
|USE_TZ|TRUE|BOOLEAN|

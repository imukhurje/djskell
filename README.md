# djSkell

## Getting Started

1. Go to https://www.thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/ and follow the top portion of the page to create a virtual env for your project.
2. Make necessary changes to /skellsite/wsgi.py
3. Make necessary changes to apache/yourdomain.com.conf and copy it to /etc/apache2/sites-enabled and do

```
sudo apachectl graceful
```

4. Install dependencies

``` 
pip install -r requirements.txt
```
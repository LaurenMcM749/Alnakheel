# arabic_magazine


### Deployment

1. Ensure makemigrations has been run and all changes are committed to git.
1. Push to Heroku:
    `git push heroku master`
1. Run migrations
    `heroku run python manage.py migrate`
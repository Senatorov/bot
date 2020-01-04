push heroku:
----------------------------------------------------------------------------------
git init | 
git status |
git add |
git commit -m '' |
heroku create 'name_project' --buildpack heroku/python --region eu |
git push heroku master |


start bot:
-----------------------------------------------------------------------------------
heroku ps:scale bot=1 |
heroku ps |

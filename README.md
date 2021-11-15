<h1 align="center">Instagram Unfollow Bot</h1>

<p align="center">This is a tool that allows a user to scan through their existing Following list to identify accounts that are not following them back.</p>

### Links

- [Repo](https://github.com/Stevie93/Instagram-Unfollow-Bot "Instagram Unfollow Bot")
- [Bugs](https://github.com/Stevie93/Instagram-Unfollow-Bot/issues "Issues Page")

### Built With

- Python
- Selenium webdriver

### Direction For Use

Install the Selenium Webdriver (chrome). [More Info](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver "Chrome Webdriver")

Enter your password in the [secrets.py](https://github.com/Stevie93/Instagram-Unfollow-Bot/blob/main/secrets.py "secrets.py") file.

``` python
pw = ''
```

In the [app.py](https://github.com/Stevie93/Instagram-Unfollow-Bot/blob/main/app.py "app.py") file, enter your username in the `Instabot` function at the bottom of the file.

```python
my_bot = InstaBot('', pw)
my_bot.get_unfollowers()
```

execute the [app.py](https://github.com/Stevie93/Instagram-Unfollow-Bot/blob/main/app.py "app.py") file.

### Author

**SFM**

### 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!

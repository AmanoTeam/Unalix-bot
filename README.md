<h2 align='center'>Unalix-bot</h2>

### What is it?

Unalix-bot is a bot developed for Telegram. Its main purpose is to help users remove tracking fields from URLs. This project is based on [ClearURLs](https://gitlab.com/KevinRoebert/ClearUrls), an add-on developed for [Chrome](https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk), [Firefox](https://addons.mozilla.org/addon/clearurls) and [Edge](https://microsoftedge.microsoft.com/addons/detail/mdkdmaickkfdekbjdoojfalpbkgaddei).

### What it does?

In addition to removing tracking fields from URLs, Unalix also try to gets the direct link from shortened URLs.

### Why would this be useful to me?

#### Privacy

It is quite common to share links within Telegram, whether they are conversations with other users or within groups. Most people don't check links before sending them, they just copy and paste. This is the biggest problem.

Links we share may contain tracking parameters related to services such as [Google Analytics](https://en.wikipedia.org/wiki/UTM_parameters) or [Google Ads](https://en.wikipedia.org/wiki/Google_Ads). The sole purpose of these parameters is to track and collect information about our online browsing.

By sharing links like these, we are not only compromising our privacy, but we are also compromising the privacy of users who click on the link sent by us. To avoid this, it is always necessary to check a link before sending them. We must analyze and remove the tracking parameters present in it.

#### It is simple and fast

Analyzing and removing tracking parameters can be a very difficult and complicated task. Depending on the size of the link and/or the number of characters in it, it is not clear which fields are being used for online tracking purposes and which are not.

Unalix has a list of specific rules that aims to remove these tracking parameters. They can remove all tracking fields (or most of it) without breaking the link.

### How to use?

It is extremely simple to use Unalix. To start using it, [open a chat](https://t.me/Unalix_bot) with the bot on Telegram and click "**START**".

From there, send via a message the link you want to be "clean". Unalix will begin processing your request and within a few seconds, it will send you the final result.

In order to be able to identify the link contained in the message, it must be in the following format:

* It must start with `http://` or `https://` (case-sensitive)

Unalix also supports inline queries. To use it, open a chat on Telegram and type `@Unalix_bot` in the message field.

### Is the bot safe?

* Unalix does not permanently store or collect sent links/messages.

* We do not send spam, advertisements or anything unrelated to the bot's primary purpose to its users.

### Limitations

Unalix has some limitations related to link processing, see them below:

 - Getting direct links from URL shorteners
  - Unalix only follows the URLs/paths provided by the `Location` header (see [RFC 7231, section 7.1.2: Location](https://tools.ietf.org/html/rfc7231#section-7.1.2)). It means that Unalix cannot obtain direct links from URL shorteners that require user interaction (e.g clicking a button or resolving CAPTCHA) to redirect or that uses JavaScript code to redirect.

## For developers

Unalix is ​​written in Python. To find out how to run it in your operating environment, follow the instructions below.

### Installation

Install all required modules/dependencies using `pip`:

```
pip3 install --upgrade 'pyTelegramBotAPI' 'Unalix'
```

### Get the source

To get Unalix source code, clone the repository using `git` or download using ` wget`.

**Clone using git:**

```
$ git clone --branch 'master' 'https://github.com/AmanoTeam/Unalix.git' ~/Unalix
```

or

**Download with wget and extract all files:**

```
$ wget 'https://codeload.github.com/AmanoTeam/Unalix-bot/tar.gz/master' --output-document 'Unalix.tar.gz'
$ tar --extract --file='Unalix.tar.gz'
$ mv 'Unalix-master' 'Unalix'
```
### Setup the bot

In the [settings.py](settings.py#L3) file, on line 3, there is the following content:

```
bot = telebot.TeleBot('TOKEN_GOES_HERE')
```

Open the file with a text editor and replace `TOKEN_GOES_HERE` by the token of your bot.

### Start the bot

Start the bot with

```
$ cd 'Unalix'
$ python3 'bot.py'
```

From that moment, the bot should already be receiving and processing the messages sent by the users (if any).

**Note**: If you want your bot to be able to process [inline queries](https://core.telegram.org/bots/inline), enable them in your bot settings (Bot Settings > Inline Mode > Turn on).

## Contact

Want to say something? Need some help? [Open a issue](https://github.com/AmanoTeam/Unalix-bot/issues) or [send a email](https://spamty.eu/show.php?key=d7967f0e625c5f19c9c655b8).

## License

Unalix-bot is licensed under the [GNU Lesser General Public License v3.0](https://github.com/AmanoTeam/Unalix-bot/blob/master/LICENSE).

## Third party software

Unalix-bot includes some third party software. See them below:

- **pyTelegramBotAPI**
  - Author: FrankWang ([eternnoir](https://github.com/eternnoir))
  - Repository: [eternnoir/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
  - License: [GNU General Public License v2.0](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/LICENSE)

- **Unalix**
  - Author: SnwMds ([SnwMds](https://github.com/SnwMds))
  - Repository: [AmanoTeam/Unalix](https://gitlab.com/AmanoTeam/Unalix)
  - License: [GNU Lesser General Public License v3.0](https://github.com/AmanoTeam/Unalix/blob/master/LICENSE)

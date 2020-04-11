<h2 align='center'>Unalix</h2>

### What is it?

Unalix is a bot developed for Telegram. Its main purpose is to help users remove tracking fields from URLs. This project is based on [ClearURLs](https://gitlab.com/KevinRoebert/ClearUrls), an add-on developed for [Chrome](https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk) and [Firefox](https://addons.mozilla.org/addon/clearurls).

### What it does?

#### 

In addition to removing tracking fields from user-submitted URLs, Unalix also try to gets the direct link from shortened URLs. Example: If you send a shortened URL from services like [bit.ly](https://bitly.com) or [goo.gl](https://goo.gl), the bot will return you the URL to which the original link redirects, not the `bit.ly` or `goo.gl` URL.

### Why would this be useful to me?

#### Privacy

It is quite common to share links within Telegram, whether they are conversations with other users or within groups. Most people don't check links before sending them, they just copy and paste. This is the biggest problem.

Links we share may contain tracking parameters related to services such as [Google Analytics](https://en.wikipedia.org/wiki/UTM_parameters) or [Google Ads](https://en.wikipedia.org/wiki/Google_Ads). The sole purpose of these parameters is to track and collect information about our online browsing.

By sharing links like these, we are not only compromising our privacy, but we are also compromising the privacy of users who click on the link sent by us. To avoid this, it is always necessary to check a link before sending them. We must analyze and remove the tracking parameters present in it.

#### It is simple and fast

Analyzing and removing tracking parameters can be a very difficult and complicated task. Depending on the size of the link and/or the number of characters in it, it is not clear which fields are being used for online tracking purposes and which are not.

Unalix has a list of specific rules ([data.min.json](rules/data.min.json) and [custom-data.min.json](rules/custom-data.min.json)) that aims to remove these tracking parameters. They can remove all tracking fields without breaking the link.

### How to use?

It is extremely simple to use Unalix. To start using it, [open a chat](https://t.me/Unalix_bot) with the bot on Telegram and click "**START**".

From there, send via a message the link you want to be "clean". Unalix will begin processing your request and within a few seconds, it will send you the final result.

In order to be able to identify the link contained in the message, it must be in the following format:

* It must start with `http://` or `https://` (case-sensitive)

_Unalix also supports inline queries. To use it, open a chat on Telegram and type `@Unalix_bot` in the message field._

### Is the bot safe?

* Unalix does not permanently store or collect sent links/messages.

* We do not send spam, advertisements or anything unrelated to the bot's primary purpose to its users.

## Limitations

Unalix has some limitations related to link processing, see them below:

### Getting direct links from URL shorteners

- Unalix only follows the URLs/paths provided by the `Location` header
   - It means that Unalix cannot obtain direct links from URL shorteners that require user interaction (e.g clicking a button or resolving CAPTCHA) to redirect or that uses JavaScript code to redirect.

## For developers

Unalix is ​​written in Python. To find out how to run it in your operating environment, follow the instructions below.

### Installation

Install all required modules/dependencies using `pip`:

```
pip3 install --upgrade 'pyTelegramBotAPI'
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
$ wget 'https://codeload.github.com/AmanoTeam/Unalix/zip/master' --output-document ~/Unalix.zip
$ unzip 'Unalix.zip' && rm -f 'Unalix.zip'
$ mv 'Unalix-master' 'Unalix'
```
### Setup the bot

In the [Unalix.py](Unalix.py#L7) file, on line 7, there is the following content:

```
bot = telebot.TeleBot('YOUR_TOKEN_HERE')
```

Open the file with a text editor and replace `YOUR_TOKEN_HERE` by the token of your bot.

### Start the bot

Start the bot with

```
$ cd ~
$ python3 ~/Unalix/Unalix.py
```

From that moment, the bot should already be receiving and processing the messages sent by the users (if any).

**Note**: If you want your bot to be able to process [inline queries](https://core.telegram.org/bots/inline), enable them in your bot settings (Bot Settings > Inline Mode > Turn on).

## Contact

Want to say something? Need some help? [Open a issue](https://github.com/AmanoTeam/Unalix/issues) or [send a email](http://scr.im:80/SnwMds).

## License

Unalix in licensed under the [GNU Lesser General Public License v3.0](https://github.com/AmanoTeam/Unalix/blob/master/LICENSE).

## Third party software

Unalix includes some third party software. See them below:

- **pyTelegramBotAPI**
  - Author: FrankWang ([eternnoir](https://github.com/eternnoir))
  - Repository: [eternnoir/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
  - License: [GNU General Public License v2.0](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/LICENSE)

- **ClearURLs**
  - Author: Kevin Röbert ([KevinRoebert](https://gitlab.com/KevinRoebert))
  - Repository: [KevinRoebert/ClearUrls](https://gitlab.com/KevinRoebert/ClearUrls)
  - License: [GNU Lesser General Public License v3.0](https://gitlab.com/KevinRoebert/ClearUrls/blob/master/LICENSE)

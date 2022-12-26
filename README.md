# Need Content System
### Sections:
* [About](#about)  
* [Dependencies](#dependencies)  
* [License, Creator, and Contact Information](#license-creator-and-contact-information)  
* [Installation](#installation)  
* [Basic Usage](#basic-usage)  
* [Configuring your Website](#configuring-your-website)  
* [Creating Content](#creating-content)
## About
Need Content System is a lightweight and easy to use content management system for quickly compiling markdown into a static, easy-to-use, easy-to-view, and browsable web app.  
Need Content System, or NCS or Need for short, can be used for research articles, blogs, short stories, design documents, or anything else.  
More information is available at https://need.cab
#
## Dependencies
#### Required:
1) Python 3.10.9 and above
2) Markdown - https://pypi.org/project/Markdown/
#
## License, Creator, and Contact Information
* Aaron Steinberg
	* aaron@aa.codes
* MIT License
	* Full License Text available in ```LICENSE```
#
## Installation
```Instructions Coming Soon```
#
## Basic Usage
1) Navigate to a directory you wish to create a Need project directory
2) Create the project  
```need create [project_name] [author_name]```
3) Navigate to the directory  
```cd [project_name]```
	* Within this directory, you will find the following files:
		### Editable Files: 
		* README.md - A template for a Need project
		* config.yaml - Configuration File
		* sources/ - Directory containing user-made source files used to generate website
		### Non Editable Files:
		* LICENSE - MIT License
		* style.css - Generated Style Sheet
		* index.html - This is the generated landing page of the website. Layout, design, and functionality can be edited from config.yaml
		* n/ 0 Each file in this directory is a generated page

4) While in the project directory, generate the site by running the following command:  
``` need gen ```  
This command will potentially change the following files:
	* **index.html**
		* This file will be overwritten with a newly generated landing page
	* **n/**
		* This directory will contain one generated html page for each user-created file in <b>sources/</b>
## Configuring your website
The default config.yaml looks like this:
```yaml
# Required Settings:

title: My Need Content System Project
author: John Smith
url: localhost
global-font-size: 1rem
source-directory-name: source
generated-directory-name: n

# Optional Settings: (any omitted boolean settings will be assumed false)

enable-about-page: true
enable-nav-bar: true

show-title-banner: true

# custom-css-file-name: [filename]
# custom-script-file-name: [filename]
```
Changing the configuration file can alter the look and feel of your project.  
Style, organization, and more can be customized to fit your needs from this file.  
### Additional properties you can add:
```yaml
non-working-property-one: test_value
```
## Creating Content
1) Navigate to the project directory
2) Navigate to the *sources* directory
3) From here, you can create one of two types of content:
	* page
	* post
4) To create a contact page, run the command:  
```need new page contact```
	* This will create a new file named **contact.page.nd**
	* Note the extension is **nd** not 'md'. This is not a typo. Need pages and posts follow a specific, custom format known as **Need**, which is shortened to **.nd**
	* Make sure you run the command from the *sources* directory 
5) Open contact.page.nd and you will see the following:
```yaml
{{
need: {
	content_type: 'page',
	title: 'Contact',
	example-constant: 'example',
	text-align: 'left',
	enable: true,
	inherit-global-constants: true,
}
}}
# {{title}}
Welcome to the {{title}} page. You can use markdown syntax freely.
## Local Constants:
You can use defined constants such as {{example_constant}}. Is this page enabled?  
{{enable ? 'yes it is' : 'no it is not'}}.
## Global Constants:
You can access global constants defined in the config file. For example, the title of the website is {{global.title}}. The author of the website is {{global.author}}
```
6. We can refactor this to make it look more like a contact page, as shown below
```yaml
{{
need: {
content_type: 'page',
title: 'Contact',
full-name: 'Bobby Robert',
phone-number: '310-555-5555',
image-path: '../assets/headshot.jpg',
text-align: 'center',
enable: true,
inherit-global-constants: true,
}
}}
# Contact Information
![headshot]({{image-path}})
* Name: {{full-name}}
* Phone:  {{phone-number}}
```

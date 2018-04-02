# Log-Analysis
This is a project for Udacity's Nanodegree Developer Web Full-Stack Program.
The objective of this project is create an analysis of a specific database about articles website.
The database is composed with three different tables which is inside the *news* database: *Articles, Authors and Log.*

*Articles* table contains informations about the articles itself, like title, time creation and also who created the article, the author.

*Authors* table contains the name and a bio about the author.

*Log* table contains informations about the access that articles had been like status request, request time and path through the article.

The analysis was create to answer this question:

    1 - What are the most popular articles of all time?
    2 - Who are the most popular authors of all time?
    3 - On which days did more than percent of requests lead to errors?

To reach the objetive of this project, *PostgreSQL* and *Python3*, both of them were installed in a virtual machine using *Virtual Box* with *Vagrant*.

## Configuring the environmenxt.
*All files needed are found on root folder of this project.*

First of all, you need to install *VirtualBox*. You can find it [here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
### Why?
As it was previously mentioned, the reason we need to have *VirtualBox* installed is the fact that it's the software actually runs the virtual machine.

After, we will need to install *Vagrant*, which you can download [here.](https://www.vagrantup.com/downloads.html)

Once you have *VirtualBox* and *Vagrant* installed, you can download the unzip the flie *fsnd-virtual-machine.zip* and after run  ```vagrant up``` to install to vagrant machine.
To have access to your virtual machoine, you can use ```vagrant ssh```. for more information about *vagrant* click [here.](https://www.vagrantup.com/)

### Importing the data.
To use this to project properly, we have import the data to our database inside the *vagrant* machine.
To do this, you have to extract the *newsdata.zip* file inside your vagrant folder and, after that, you can run this command in your terminal: ```psql -d news -f newsdata.sql```. THis command will import all the data inside the *news* database.

## Running the app.
Once you finish the configuration steps. you have to run:
```
python3 news_report_tool.py
```
This command will print some question from analysis database with it's answers.

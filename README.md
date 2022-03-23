## Conclusions

IPynb-file has been provided for showcasing the projects features and also to provide clear overview about them. 
Income growth has been highest in area <mark>16710  Hollola kk (Hollola) observed growth has been 19.982818 percent.</mark> Growth has been steady in the past five years.

Some other areas such as Kaartinkaupunki the growth has been recently declining. It might something to do with pandemic when
People are looking for more spacious apartments. Also, there has been growth in smaller areas during the same time which can additionally support the hypothesis that people are moving away from city centers where apartments can be quite small.

### Script's properties

5 individual JSON-queries which are stored in parser function which generates new listis. A function which generates SQLite-database. A plotter function which iterates over parser-functions lists and generates the wanted information and visualizes them. Lastly, a main-function which calls all aforementioned functions.
### Technical notes

There is a possibility to automate this script to update every March. It will need a designated function which checks the time and generates new JSON-query. This function will also generate a new SQLite-table and update the Zip-code index from five to six.
However, the major design flaw of this script is that there are five different JSON-queries which affect in part for some of the script's design. Paavo-APi uses distinct urls to get the wanted queries and due to writers inexperience using the API, a solution for a single API call to get the wanted information was not found. This should be fixed first. Then update the code to get rid of five different dataframes and instead use only one. After these steps, the designated updater-function can be constructed properly. 
Lastly, Pandas Dataframe could have been used to store the JSON-querys. This is something that must be learned for the future.  

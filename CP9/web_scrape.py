import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_selector_table():
    """
    Reads a webpage and extracts out the contents of a table.
    https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#reference_table_of_selectors

    Returns a dataframe with the content:
    Selector            Example        Description
    .class	            .intro	       Selects all elements with class="intro"
    .class1.class2	    .name1.name2   Selects all elements with both name1 and name2...
    .class1 .class2	    .name1 .name2  Selects all elements with name2 that is a desc...
    #id	                #firstname	   Selects the element with id="firstname"
    <60 rows>
    """
    url = "https://www.w3schools.com/cssref/css_selectors.asp"
    page = requests.get(url)
    # create a beautiful soup object that can parse the HTML content
    full_of_soup = BeautifulSoup(page.content, "html.parser")

    # get the table markup from soup object
    table = full_of_soup.find("table")

    # parse the 3 columns by getting the <td> data that is a child of <tr>
    rows = table.find_all("tr")[1:]

    # create a list for each column, getting the text content as needed
    selectors: list[str] = []
    examples: list[str] = []
    descriptions: list[str] = []

    for row in rows:
        tds = row.find_all("td")
        selectors.append(tds[0].text)
        examples.append(tds[1].text)
        descriptions.append(tds[2].text)

    # Create and return a dataframe using the lists created above
    df = pd.DataFrame(
        {
            "Selector": selectors,
            "Example": examples,
            "Description": descriptions,
        }
    )

    return df


def main():
    print(get_selector_table())


if __name__ == "__main__":
    main()

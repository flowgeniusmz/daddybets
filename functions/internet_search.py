import streamlit as st
from tavily import TavilyClient

class InternetSearch:
    def __init__(self, api_key):
        """
        Initializes the InternetSearch with a TavilyClient.

        Parameters:
        api_key (str): API key for the TavilyClient.
        """
        self.client = TavilyClient(api_key=st.secrets.tavily.api_key)

    def search(self, varQuery, varType='basic'):
        """
        Conducts an internet search based on a query and a specified search type.

        Parameters:
        varQuery (str): The query string for the internet search.
        varType (str, optional): The type of the search. Can be either 'basic' or 'advanced'.
                                 Defaults to 'basic'.

        Raises:
        ValueError: If varType is not 'basic' or 'advanced'.

        Returns:
        The result of the internet search. (Customize based on actual function return)
        """
        if varType not in ['basic', 'advanced']:
            raise ValueError("varType must be either 'basic' or 'advanced'.")

        search_result = self.client.get_search_context(
            query=varQuery,
            search_depth=varType,
            max_tokens=4000,
            max_results=5
        )
        return search_result

    # Example method for a different type of search or functionality
    def advanced_search(self, varQuery, additional_params):
        """
        Conducts an advanced internet search with additional parameters.

        Parameters:
        varQuery (str): The query string for the internet search.
        additional_params (dict): Additional parameters for the search.

        Returns:
        The result of the advanced internet search. (Customize based on actual function return)
        """
        # Example of using additional_params in a search
        search_result = self.client.get_search_context(
            query=varQuery,
            **additional_params
        )
        return search_result

# Usage example
# Initialize with your API key
searcher = InternetSearch(api_key="your_api_key_here")

# Basic search
basic_result = searcher.search("example query")

# Advanced search
advanced_result = searcher.advanced_search("example query", {"extra_param": "value"})

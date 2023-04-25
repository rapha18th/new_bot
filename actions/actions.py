import pandas as pd
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List


class GetCustomerWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_customer_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        # Get customer with most sales
        customer = df.loc[df['Sale'].idxmax()]['Customer Name']

        # Send result to user
        dispatcher.utter_message(text=f'Customer with most sales: {customer}')

        return []


class GetRouteWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_route_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        # Get route with most sales
        route = df.loc[df['Sale'].idxmax()]['Route']

        # Send result to user
        dispatcher.utter_message(text=f'Route with most sales: {route}')

        return []


class GetRouteWithLeastSales(Action):
    def name(self) -> Text:
        return "action_get_route_with_least_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        # Get route with most sales
        route = df.loc[df['Sale'].idxmin()]['Route']

        # Send result to user
        dispatcher.utter_message(text=f'Route with least sales: {route}')

        return []


class GetMonthWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_month_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        # Get month with most sales
        month = df.loc[df['Sale'].idxmax()]['Month']

        # Send result to user
        dispatcher.utter_message(text=f'Month with most sales: {month}')

        return []


class GetAverageRevenue6months(Action):
    def name(self) -> Text:
        return "action_get_average_revenue_last_6_months"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #convert Month column to datetime format


        df['Month'] = pd.to_datetime(df['Month'], format='%B')

        df = df.sort_values(by='Month')

      # get last 6 months
        last_6_months = df['Month'].unique()[-6:]

      # filter dataframe by last 6 months
        df = df[df['Month'].isin(last_6_months)]

      # calculate average revenue
        average_revenue = df['Sale'].mean()


        # Send result to user
        dispatcher.utter_message(text=f'In the last 6 months the average revenue was: {average_revenue}')

        return []


class GetAverageRevenue9months(Action):
    def name(self) -> Text:
        return "action_get_average_revenue_last_9_months"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #convert Month column to datetime format
        df = pd.read_csv('adc.csv')

        df['Month'] = pd.to_datetime(df['Month'], format='%B')

        df = df.sort_values(by='Month')

      # get last 6 months
        last_9_months = df['Month'].unique()[-9:]

      # filter dataframe by last 6 months
        df = df[df['Month'].isin(last_9_months)]

      # calculate average revenue
        average_revenue = df['Sale'].mean()

        # Send result to user
        dispatcher.utter_message(
            text=f'In the last 9 months the average revenue was: {average_revenue}')

        return []


class GetAverageRevenue12months(Action):
    def name(self) -> Text:
        return "action_get_average_revenue_last_12_months"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #convert Month column to datetime format
        df = pd.read_csv('adc.csv')

        df['Month'] = pd.to_datetime(df['Month'], format='%B')

        df = df.sort_values(by='Month')

      # get last 6 months
        last_12_months = df['Month'].unique()[-12:]

      # filter dataframe by last 6 months
        df = df[df['Month'].isin(last_12_months)]

      # calculate average revenue
        average_revenue = df['Sale'].mean()

        # Send result to user
        dispatcher.utter_message(
            text=f'In the last 12 months the average revenue was: {average_revenue}')

        return []


class GetAverageRevenue3months(Action):
    def name(self) -> Text:
        return "action_get_average_revenue_last_3_months"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #convert Month column to datetime format
        df = pd.read_csv('adc.csv')

        df['Month'] = pd.to_datetime(df['Month'], format='%B')

        df = df.sort_values(by='Month')

      # get last 6 months
        last_3_months = df['Month'].unique()[-3:]

      # filter dataframe by last 6 months
        df = df[df['Month'].isin(last_3_months)]

      # calculate average revenue
        average_revenue = df['Sale'].mean()

        # Send result to user
        dispatcher.utter_message(
            text=f'In the last 3 months the average revenue was: {average_revenue}')

        return []


class GetMonthsWithLowestOutliers(Action):
    def name(self) -> Text:
        return "action_get_months_with_highest_outliers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #convert Month column to datetime format
        df = pd.read_csv('adc.csv')


        # convert Month column to datetime format
        df['Month'] = pd.to_datetime(df['Month'], format='%B')

        # calculate z-score for Sale column
        df['z_score'] = (df['Sale'] - df['Sale'].mean()) / df['Sale'].std()

        # find months with highest outliers
        months_with_outliers = df.groupby(
    'Month')['z_score'].apply(lambda x: x[x > 3].count())


        dispatcher.utter_message(
            text=f'Months with highest outliers: {months_with_outliers}')

        return []


class GetTotalNumberOfCustomers(Action):
    def name(self) -> Text:
        return "action_get_total_customers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_excel("craig_product.xlsx", engine="openpyxl")

        total_num_customers = df['Reference'].nunique()

        customers = total_num_customers

        dispatcher.utter_message(
            text=f'Total Number Of Customers: {customers}')

        return []


class GetRepWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_rep_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        sales_by_rep = df.groupby('Rep Code')['Sale'].sum()


# Find rep code with lowest sales
        agent = sales_by_rep.idxmax()

        # Send result to user
        dispatcher.utter_message(text=f'Sales Agent with the most sales: {agent}')

        return []


class GetRepWithLeastSales(Action):
    def name(self) -> Text:
        return "action_get_rep_with_least_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        sales_by_rep = df.groupby('Rep Code')['Sale'].sum()


# Find rep code with lowest sales
        agent = sales_by_rep.idxmin()


        # Send result to user
        dispatcher.utter_message(
            text=f'Sales Agent with the least sales: {agent}')

        return []


class GetCustomerWithHighestProfitValue(Action):
    def name(self) -> Text:
        return "action_get_customer_with_highest_profit_value"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel('craig_tour.xlsx', engine="openpyxl")

        # Get customer with most sales
        customer = df.loc[df['Profit Value'].idxmax()]['BookingName']

        # Send result to user
        dispatcher.utter_message(text=f'Customer with the highest profit value: {customer}')

        return []


class GetAgentWithLeastSales(Action):
    def name(self) -> Text:
        return "action_get_agent_with_least_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel('craig_tour.xlsx', engine="openpyxl")

        sales_by_rep = df.groupby('AgentName')['Cost'].sum()


# Find rep code with lowest sales
        agent = sales_by_rep.idxmin()

        # Send result to user
        dispatcher.utter_message(
            text=f'Sales Agent with the least sales: {agent}')

        return []

class GetAgentWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_agent_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel('craig_tour.xlsx', engine="openpyxl")

        sales_by_rep = df.groupby('AgentName')['Cost'].sum()


# Find rep code with lowest sales
        agent = sales_by_rep.idxmax()

        # Send result to user
        dispatcher.utter_message(
            text=f'Sales Agent with the most sales: {agent}')

        return []

class GetMonthsWithHighestOutliers(Action):
    def name(self) -> Text:
        return "action_get_months_with_highest_outliers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv('adc.csv')

        # convert Month column to datetime format
        df['Month'] = pd.to_datetime(df['Month'], format='%B')

# sort dataframe by Month column
        df = df.sort_values(by='Month')

# calculate z-score for Sale column
        df['z_score'] = (df['Sale'] - df['Sale'].mean()) / df['Sale'].std()

# find months with highest outliers
        months_with_outliers = df.groupby('Month')['z_score'].apply(lambda x: x[x > 3].count())
        months = months_with_outliers
        print(f'Months with highest outliers:\n{months_with_outliers}')

        # Send result to user
        dispatcher.utter_message(
            text=f'Months with the highest outliers adc data: {months}')

        return []


class GetQVariance(Action):
    def name(self) -> Text:
        return "action_get_q_variance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel("craig_product.xlsx", engine="openpyxl")

        df['Date'] = pd.to_datetime(df['Date'], format='%B')


        df['date'] = pd.to_datetime(df['Date'])

# Set date column as index
        df.set_index('date', inplace=True)

# Resample data by annual period
        q_sales = df.resample('Q').sum()

# Calculate annual sales variance
        q_sales_variance = q_sales.pct_change().var()

        variance = q_sales_variance

        # Send result to user
        dispatcher.utter_message(
            text=f'This is the quarterly variance for sales and selected variables: {variance}')

        return []


class Get2QVariance(Action):
    def name(self) -> Text:
        return "action_get_2q_variance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel("craig_product.xlsx", engine="openpyxl")

        df['Date'] = pd.to_datetime(df['Date'], format='%B')

        df['date'] = pd.to_datetime(df['Date'])

# Set date column as index
        df.set_index('date', inplace=True)

# Resample data by annual period
        q2_sales = df.resample('Q').sum()

# Calculate annual sales variance
        q2_sales_variance = q2_sales.pct_change().var()
        variance = q2_sales_variance
        # Send result to user
        dispatcher.utter_message(
            text=f'This is the bi_annual variance for sales and selected variables: {variance}')

        return []

class GetYVariance(Action):
    def name(self) -> Text:
        return "action_get_y_variance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel("craig_product.xlsx", engine="openpyxl")

        df['Date'] = pd.to_datetime(df['Date'], format='%B')


        df['date'] = pd.to_datetime(df['Date'])

# Set date column as index
        df.set_index('date', inplace=True)

# Resample data by annual period
        y_sales = df.resample('y').sum()

# Calculate annual sales variance
        y_sales_variance = y_sales.pct_change().var()

        variance = y_sales_variance

        # Send result to user
        dispatcher.utter_message(
            text=f'This is the yearly variance for sales and selected variables: {variance}')

        return []

class GetSupplierWithMostSales(Action):
    def name(self) -> Text:
        return "action_get_supplier_with_most_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel('craig_product.xlsx', engine="openpyxl")

        sales_by_rep = df.groupby('SupplierName')['Cost'].sum()


# Find rep code with lowest sales
        supplier = sales_by_rep.idxmax()

        # Send result to user
        dispatcher.utter_message(
            text=f'Supplier with the most sales: {supplier}')

        return []

class GetSupplierWithLeastSales(Action):
    def name(self) -> Text:
        return "action_get_supplier_with_least_sales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Read CSV file into a pandas DataFrame
        df = pd.read_excel('craig_product.xlsx', engine="openpyxl")

        sales_by_rep = df.groupby('SupplierName')['Cost'].sum()


# Find rep code with lowest sales
        supplier = sales_by_rep.idxmin()

        # Send result to user
        dispatcher.utter_message(
            text=f'Supplier with the least sales: {supplier}')

        return []


class GetTotalNumberOfSuppliers(Action):
    def name(self) -> Text:
        return "action_get_total_suppliers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_excel("craig_product.xlsx", engine="openpyxl")

        total_num_customers = df['SupplierName'].nunique()

        customers = total_num_customers

        dispatcher.utter_message(
            text=f'Total Number Of Supplierss: {customers}')

        return []

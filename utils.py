import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#A helper function to convert a string to camel case
def to_snake_case(input_string):
    # Convert to lowercase
    lower_case_string = input_string.lower()
    # Remove non-alphanumeric characters except spaces
    cleaned_string = re.sub(r'[^a-z0-9\s]', '', lower_case_string)
    # Replace spaces with underscores
    snake_case_string = re.sub(r'\s+', '_', cleaned_string)
    return snake_case_string

#Util function that counts the number of accepted and rejected coupons for a dataframe
def count_acceptance(df):
    # Calculate the total number of observations
    total_observations = df['y'].count()

    # Calculate the number of observations where the coupon was accepted
    accepted_coupons = df[df['y'] == 1]['y'].count()

    # Calculate the number of observations where the coupon was not accepted
    rejected_coupons = total_observations - accepted_coupons

    return  {
        'accepted': accepted_coupons, 
        'rejected':rejected_coupons,
        'total':total_observations
    }
    
#Util function that creates a combined pie and bar graph
#Pie: Shows accepted vs rejected percentage for dataframe and coupon type
#Bar: shows total accpeted vs total rejected
def plot_coupon_acceptance(df, coupon_type):

    #calculate values
    calculated_values = count_acceptance(df)

    # Data for the plot
    labels = ['Accepted', 'Not Accepted']
    sizes = [calculated_values['accepted'], calculated_values['rejected']]
    colors = ['#4CAF50', '#FF5733']

    # Plotting the pie chart
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'Proportion of {coupon_type} Coupon Acceptance')

    # Plotting the bar chart
    plt.subplot(1, 2, 2)
    plt.bar(labels, sizes, color=colors)
    plt.title(f'{coupon_type} Coupon Acceptance Counts')
    plt.ylabel('Number of Observations')

    # Show the plots
    plt.tight_layout() #cleans up the size of fonts and spacing.
    plt.savefig(f'images/{to_snake_case(coupon_type)}_coupon_acceptance.png')
    plt.show()


# def plot_comparison( 
    #     categories, 
    #     option_1_df, 
    #     options_2_df,
    #     title,
    #     xlabel,
    #     ylabel,
    # ):
    # option_1_rates = count_acceptance(option_1_df)
    # option_2_rates = count_acceptance(options_2_df)

    # # Plot graph( using seaborn for some variation)
    # plot_data = {
    #     'Categories':categories, 
    #     'Acceptance Rates': [
    #         (option_1_rates['accepted'] / option_1_rates['total'])*100,
    #         (option_2_rates['accepted']/option_2_rates['total'])*100
    #     ]
    # }
    # plot_dataframe = pd.DataFrame(plot_data)

    # # Create figure with specified size
    # plt.figure(figsize=(10, 6))

    # # Create bar graph
    # colors = ['#4CAF50', '#FF5733'] #Bar colors
    # barplot = sns.barplot(x='Categories', y='Acceptance Rates', data=plot_dataframe, palette=colors)

    # # Set labels and title
    # plt.xlabel(xlabel)
    # plt.ylabel(ylabel)
    # plt.title(title)

    # # Format y-axis as percentages
    # barplot.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    # plt.ylim(0, 100)

    # # Save the plot to /images directory
    # plt.tight_layout()
    # plt.savefig(f'images/{to_snake_case(title)}.png')

    # # Show the graph
    # plt.show()



def plot_comparison(
        categories, 
        options, 
        title, 
        xlabel, 
        ylabel
    ):
    acceptance_rates = []
    
    # Calculate acceptance rates for each option
    for option_df in options:
        rates = count_acceptance(option_df)
        acceptance_rate = (rates['accepted'] / rates['total']) * 100
        acceptance_rates.append(acceptance_rate)
    
    # Plot graph( using seaborn for some variation)
    plot_data = {
        'Categories': categories, 
        'Acceptance Rates': acceptance_rates
    }
    plot_dataframe = pd.DataFrame(plot_data)
    
    # Create figure with specified size
    plt.figure(figsize=(10, 6))
    
    # Create bar graph
    colors = sns.color_palette("husl", len(options))  # Generate colors for each option
    barplot = sns.barplot(x='Categories', y='Acceptance Rates', data=plot_dataframe, palette=colors)
    
    # Set labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # Format y-axis as percentages
    barplot.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    plt.ylim(0, 100)
    
    # Save the plot to /images directory
    plt.tight_layout()
    plt.savefig(f'images/{to_snake_case(title)}.png')
    
    # Show the graph
    plt.show()

# Example usage:
# categories = ['Category1', 'Category2']
# options = [option_1_df, option_2_df, option_3_df]
# plot_comparison(categories, options, "Comparison Title", "X Axis Label", "Y Axis Label")

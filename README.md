# WhatsApp Chat Analyzer

🚀 Excited to share my latest project: WhatsApp Chat Analyzer! 📊🔍

This Python-powered tool leverages machine learning and Streamlit to provide comprehensive insights into both personal and group WhatsApp chats. Simply export your chat in .txt format and let the analyzer do the rest.

## Features

1. **Top Statistics**: Total messages, words, media, and links shared.
2. **Most Busy Users**: Identify the most active participants with percentages.
3. **Monthly Timeline**: Visualize message volume month by month.
4. **Daily Timeline**: See daily messaging trends with detailed graphs.
5. **Activity Map**: Discover peak chatting days and months.
6. **Weekly Activity Map**: Heatmap of the most active times during the week.
7. **WordCloud**: Visual representation of the most frequently used words.
8. **Most Common Words**: Excludes stopwords to highlight meaningful terms.
9. **Most Common Emojis**: Breakdown of emoji usage with a pie chart.
10. **Flexible Time Format**: Supports both 12-hour and 24-hour time format .txt files.

## Installation

To run this project locally, you'll need to have Python and some dependencies installed. Follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Shyam1604/WCA.git
    cd whatsapp-chat-analyzer
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure you have the following dependencies (add them to a `requirements.txt` file if you haven’t already):
    
    ```
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    wordcloud
    emoji
    ```

3. **Export WhatsApp chat**:

   - Open the chat you want to analyze in WhatsApp.
   - Tap on the chat menu (three dots) and select "More" > "Export chat".
   - Save the chat without media in .txt format.

4. **Run the application**:

    ```bash
    streamlit run app.py
    ```

5. **Open your browser** and go to `http://localhost:8501` to access the app.

## Project Structure

- `app.py`: The main application file for Streamlit.
- `helper.py`: Contains functions to assist with data analysis and visualization.
- `preprocess.py`: Handles preprocessing of chat data.
- `procfile`: Used for deployment on platforms like Heroku.

## Usage

1. **Upload your exported chat**: Click on "Browse files" in the Streamlit app to upload your exported WhatsApp chat (.txt file).

2. **Explore insights**: The app will display various statistics and visualizations about your chat, including top statistics, most busy users, timelines, activity maps, word clouds, common words, and emoji usage.

## Example

Here is an example of how the WordCloud feature looks:

![WordCloud Example](images/wordcloud_example.png)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, please open an issue or submit a pull request.

## Contact

For any questions, feel free to contact me at [shyamkalariya294@gmail.com](mailto:shyamkalariya294@gmail.com).

import streamlit as st
import matplotlib.pyplot as plt
import helper
import preprocessor

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # stats area
        num_messages , words = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1 , col2 = st.columns(2)

        with col1:
            st.header("Total Messages")
            st.header(num_messages)
        with col2:
            st.header("Total Chat Words")
            st.header(words)

        # .....
        num_media_messages, num_links = helper.fetch2_stats(selected_user, df)

        col3, col4 = st.columns(2)

        with col3:
            st.header("Media Shared")
            st.header(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.header(num_links)

        # finding the busiest user in the group
        if selected_user == 'Overall':
            st.title("Most Busy Users")
            x , new_df= helper.most_busy_users(df)
            fig , ax = plt.subplots()

            col1,col2 = st.columns(2)

            with col1:
                ax.bar(x.index,x.values,color='#D51616')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # monthly timeline
        timeline = helper.monthly_timeline(selected_user, df)
        st.title("Monthly Timeline")
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='#D51616')
        plt.xlabel('Month')
        plt.ylabel('Message Counts')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        daily_timeline = helper.daily_timeline(selected_user, df)
        st.title("Daily Timeline")
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='#D51616')
        plt.xlabel('Day')
        plt.ylabel('Message Counts')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # activity map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig , ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values,color='#D51616')
            plt.xlabel('Day')
            plt.ylabel('Message Counts')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig , ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xlabel('Month')
            plt.ylabel('Message Counts')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Wordcloud
        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig , ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        st.title("Most common words used in chat")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1],color='#D51616')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)

        #Emoji analysis
        st.title("Most common Emoji's used in chat")
        emoji_df = helper.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(8),labels=emoji_df[0].head(8),autopct = '%0.2f')
            st.pyplot(fig)


st.sidebar.write("Created By : Shyam Kalariya")
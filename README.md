
# 🎥 Video Recommendation Algorithm Assignment

## 🎯 Objective

Design a recommendation algorithm that suggests videos based on user preferences and engagement patterns. The algorithm will deliver personalized video recommendations by leveraging user interaction data and video metadata obtained via provided APIs.

## 📊 Dataset

The dataset can be fetched using the following APIs, which provide information on user interactions and video metadata:

- **Base URL**: `https://api.socialverseapp.com`

### APIs

1. **Get All Viewed Posts of Users**:
   ```
   {{base_url}}/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

2. **Get All Liked Posts of Users**:
   ```
   {{base_url}}/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

3. **Get All User Ratings**:
   ```
   {{base_url}}/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

4. **Get All Posts**:
   ```
   {{base_url}}/posts/summary/get?page=1&page_size=1000
   ```

5. **Get All Users**:
   ```
   {{base_url}}/users/get_all?page=1&page_size=1000
   ```

### Authorization

For each API request, include the following header:
- **Flic-Token**: `"flic_1e01009f9c1a54706f385bcc1993a08fd9647ba8f499572d280654d1c03c47bf"`

### Requirements

1. **Personalization:** The recommendation algorithm should make personalized suggestions based on user history and engagement patterns with similar videos.
2. **Cold Start Problem Handling:** Include a mechanism to recommend videos for new users without prior interaction history.
3. **Trending Content:** Account for recent trends and popularity boosts in recommendations.

## 🛠️ Specific Tasks

### 1. Data Preprocessing
   - Use the APIs provided to retrieve and preprocess video metadata and user interaction data.
   - Handle missing values, normalize data, and create derived features as needed for the recommendation model.

### 2. Algorithm Development
   - Develop a recommendation algorithm using approaches such as:
     - **Content-based filtering:** Recommending videos similar to those the user has viewed or liked.
     - **Collaborative filtering:** Leveraging similar user preferences to enhance recommendations.
     - **Hybrid models:** Combining content-based and collaborative filtering for improved accuracy.
   - Justify the model selection and describe how it meets the project goals.

### 3. Evaluation Metrics
   - Implement metrics to measure recommendation quality, such as:
     - **Click-through rate (CTR):** To assess user engagement.
     - **Mean Average Precision (MAP):** For ranking precision in relevance.
   - Summarize results and insights gained from metric evaluations.

### 4. Documentation
   - Provide clear, step-by-step documentation of the approach, model architecture, and key decisions made during development.
   - Discuss any challenges and solutions.

## 📦 Deliverables

1. **Preprocessed Dataset:** A dataset ready for use by the recommendation model.
2. **Codebase:** A well-documented code repository with API calls and recommendation algorithms.
3. **Evaluation Results:** Metrics showing the performance of the recommendation system.
4. **Documentation:** Explanations of the approach, model, and reasoning (README.md file).
5. **Video subbmition:** Explain your work in a video explaination with a small intro of yourself.

## 🎬 Notes

- This assignment evaluates your skills in data handling, recommendation design, and performance evaluation.
- You’re encouraged to explore additional features if they could enhance the recommendation quality.
- For any queries you can message on telegram: https://t.me/+VljbLT8o75QxN2I9
- Kindly do not ask silly question, do proper RND before asking any question, so we can give you best answer of your question.

Happy coding and good luck! 🌟

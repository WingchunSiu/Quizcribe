# Quizcribe
![屏幕截图 2024-10-20 112001](https://github.com/user-attachments/assets/bcb28a88-70d2-49b2-a65e-5ca9e130e8b4)

Calhacks 11.0 Michael Siu, Richard Peng, Yiling Yuan, Zhen Liu

## Overview
Quizcribe is an educational software that supplements students with AI-powered study resources generated from inputted videos or audio.
By entering a link to a video, such as one from YouTube, Quizcribe automatically transcribes the video, returns a detailed summary of its content, and generates an interactive quiz game for knowledge testing and review.  

Through providing a more versatile, time-efficient, and fun study medium, Quizcribe aims to expand the effectiveness of free online education, further expanding the accessibility of educational resources to people of all backgrounds. 

Main Features:
* Automated speech-to-text transcription that converts videos/audio of any length into text.
* AI-powered video summary and interactive quiz generation.
* Video detection and transcription support for 16 languages. 

## Running & Installation
To install dependencies:
```
pip install -r requirements.txt
```
```
cd calhacksmryz
npm install
```

Run App and API Server:
```
npm run dev
```
```
cd backend
python manage.py runserver
```
The app should be at `localhost:3000`

## Tech Stack
* Frontend: Next.js/React, Tailwind CSS, Material UI
* Backend: Django/Python
* API: Deepgram (Speech to Text), Google Gemini 1.5, YouTube DL

## Key Functionalities

### Video/Audio to Transcript Generation using Deepgram
* Users are prompted to input a link, which is passed to the YouTube DL and extracted into a video file URL.
* Deepgram AI's Speech-To-Text API is then used to convert the audio into transcripts.
* Deepgram AI's built-in language detection system allows for the transcription of videos/audio in 16 languages.

### Content Summarization using Google Gemini
* Gemini API is used to automatically provide consistently structured summaries for the plain text transcripts.
### Interactive Quiz Generation using Google Gemini
* Using a chain of thought approach, problem sets are generated from the summarized content. The logic behind this feature involves step-by-step prompt engineering that ensures the generated questions are relevant, thought-provoking, and aligned with the key concepts in the summarized content.
* Corrent answer are determined by AI-powered logic reasoning.

### Demo
![屏幕截图 2024-10-20 112138](https://github.com/user-attachments/assets/b9d00b12-2ddc-4c5c-958e-a594b7e33154)
_Summary to video url provided_

![image (2)](https://github.com/user-attachments/assets/e7b33303-5641-4325-8a1c-6dd0e53fd341)
_Quiz_

![image (3)](https://github.com/user-attachments/assets/293ff408-c2a7-4627-b823-908b60d44961)
_Result_

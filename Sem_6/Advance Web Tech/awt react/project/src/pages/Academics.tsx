import React from 'react';
import { BookOpen, Brain, FileText, Mic, PenTool } from 'lucide-react';

const Academics = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Academics & Learning</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* AI Study Assistant */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Brain className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">AI Study Assistant</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Get instant help with your questions and summarize your notes</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Start Conversation
          </button>
        </div>

        {/* Smart Flashcards */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <PenTool className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Smart Flashcards</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">AI-generated flashcards based on your subjects</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Create Flashcards
          </button>
        </div>

        {/* Document Reader */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <FileText className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">PDF Reader</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Upload and annotate your study materials</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Upload Document
          </button>
        </div>

        {/* Study Timetable */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <BookOpen className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Study Timetable</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Generate personalized study schedules</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Create Schedule
          </button>
        </div>

        {/* Lecture Recording */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Mic className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Lecture Recording</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Record and transcribe your lectures</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Start Recording
          </button>
        </div>
      </div>
    </div>
  );
};

export default Academics;
import React from 'react';
import { Heart, Smile, Bell, Dumbbell } from 'lucide-react';

const Wellbeing = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Well-being & Motivation</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Daily Affirmations */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Smile className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Daily Motivation</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Start your day with positive affirmations</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Get Inspired
          </button>
        </div>

        {/* Meditation & Focus */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Heart className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Focus Mode</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Meditation and focus exercises</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Start Session
          </button>
        </div>

        {/* Break Reminders */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Bell className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Break Reminders</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Stay fresh with regular breaks</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Set Reminders
          </button>
        </div>

        {/* Health Tracker */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Dumbbell className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Health Tracker</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Track exercise and water intake</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Track Health
          </button>
        </div>
      </div>
    </div>
  );
};

export default Wellbeing;
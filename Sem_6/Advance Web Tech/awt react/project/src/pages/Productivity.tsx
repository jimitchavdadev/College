import React from 'react';
import { Timer, CheckSquare, Repeat, FileEdit, HardDrive } from 'lucide-react';

const Productivity = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Productivity & Task Management</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Smart Task Manager */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <CheckSquare className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Smart Tasks</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">AI-powered task prioritization and management</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Tasks
          </button>
        </div>

        {/* Pomodoro Timer */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Timer className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Pomodoro Timer</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Stay focused with timed study sessions</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Start Timer
          </button>
        </div>

        {/* Habit Tracker */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Repeat className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Habit Tracker</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Build and maintain productive study habits</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Track Habits
          </button>
        </div>

        {/* Offline Notes */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <FileEdit className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Offline Notes</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Take notes that sync when you're back online</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Open Notes
          </button>
        </div>

        {/* Cloud Storage */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <HardDrive className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Cloud Storage</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Connect and manage your cloud storage</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Connect Drive
          </button>
        </div>
      </div>
    </div>
  );
};

export default Productivity;
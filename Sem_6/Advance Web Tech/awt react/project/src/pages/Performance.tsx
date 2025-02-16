import React from 'react';
import { LineChart, Brain, Target, Calculator } from 'lucide-react';

const Performance = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Performance Tracking & Analytics</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Grade Tracker */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <LineChart className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Grade Tracker</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Track your academic progress over time</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Analytics
          </button>
        </div>

        {/* AI Feedback */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Brain className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">AI Feedback</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Get personalized improvement suggestions</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Insights
          </button>
        </div>

        {/* Goal Setting */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Target className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Goals</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Set and track academic milestones</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Set Goals
          </button>
        </div>

        {/* GPA Calculator */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Calculator className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">GPA Calculator</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Calculate current and projected GPA</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Calculate GPA
          </button>
        </div>
      </div>
    </div>
  );
};

export default Performance;
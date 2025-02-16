import React from 'react';
import { Calendar } from 'lucide-react';

const Dashboard = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Quick Stats Widget */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Quick Stats</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-600 dark:text-gray-300">Current GPA</span>
              <span className="text-lg font-medium text-gray-900 dark:text-white">3.8</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 dark:text-gray-300">Completed Credits</span>
              <span className="text-lg font-medium text-gray-900 dark:text-white">64</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 dark:text-gray-300">Active Courses</span>
              <span className="text-lg font-medium text-gray-900 dark:text-white">5</span>
            </div>
          </div>
        </div>

        {/* Upcoming Deadlines Widget */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Upcoming Deadlines</h3>
          <div className="space-y-4">
            <div className="flex items-center">
              <Calendar className="h-5 w-5 text-indigo-500 mr-2" />
              <div>
                <p className="text-sm font-medium text-gray-900 dark:text-white">Math Assignment</p>
                <p className="text-xs text-gray-500 dark:text-gray-400">Due in 2 days</p>
              </div>
            </div>
            <div className="flex items-center">
              <Calendar className="h-5 w-5 text-indigo-500 mr-2" />
              <div>
                <p className="text-sm font-medium text-gray-900 dark:text-white">Physics Lab Report</p>
                <p className="text-xs text-gray-500 dark:text-gray-400">Due in 5 days</p>
              </div>
            </div>
          </div>
        </div>

        {/* Study Progress Widget */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Study Progress</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-1">
                <span className="text-sm text-gray-600 dark:text-gray-300">Mathematics</span>
                <span className="text-sm text-gray-600 dark:text-gray-300">75%</span>
              </div>
              <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                <div className="bg-indigo-500 h-2 rounded-full" style={{ width: '75%' }}></div>
              </div>
            </div>
            <div>
              <div className="flex justify-between mb-1">
                <span className="text-sm text-gray-600 dark:text-gray-300">Physics</span>
                <span className="text-sm text-gray-600 dark:text-gray-300">60%</span>
              </div>
              <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                <div className="bg-indigo-500 h-2 rounded-full" style={{ width: '60%' }}></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
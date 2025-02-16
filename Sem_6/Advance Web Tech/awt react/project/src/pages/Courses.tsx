import React from 'react';
import { Calendar, Upload, Users, MessageSquare, PenTool } from 'lucide-react';

const Courses = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Course Management & Collaboration</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Class Schedule */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Calendar className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Class Schedule</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">View and manage your class timetable</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Schedule
          </button>
        </div>

        {/* Assignment Submission */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Upload className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Assignments</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Submit and track your assignments</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Assignments
          </button>
        </div>

        {/* Collaboration Hub */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Users className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Collaboration</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Work together on group projects</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Join Projects
          </button>
        </div>

        {/* Chat & Forums */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <MessageSquare className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Discussion</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Chat with peers and mentors</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Open Chat
          </button>
        </div>

        {/* Virtual Whiteboard */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <PenTool className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Whiteboard</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Create diagrams and mind maps</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Open Whiteboard
          </button>
        </div>
      </div>
    </div>
  );
};

export default Courses;
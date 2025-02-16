import React from 'react';
import { Briefcase, FileText, GraduationCap, Linkedin } from 'lucide-react';

const Career = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Career & Skill Development</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Internships */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Briefcase className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Internships</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Find internships matching your skills</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Browse Listings
          </button>
        </div>

        {/* Resume Builder */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <FileText className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Resume Builder</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Create professional resumes with AI</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Build Resume
          </button>
        </div>

        {/* Skill Courses */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <GraduationCap className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Courses</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Enhance your skills with online courses</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Browse Courses
          </button>
        </div>

        {/* LinkedIn */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Linkedin className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">LinkedIn</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Sync your achievements and skills</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Connect Profile
          </button>
        </div>
      </div>
    </div>
  );
};

export default Career;
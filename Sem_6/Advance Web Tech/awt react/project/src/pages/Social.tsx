import React from 'react';
import { Calendar, Users, ShoppingBag } from 'lucide-react';

const Social = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Social & Extracurricular</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Event Calendar */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Calendar className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Events</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Track university events and meetings</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Events
          </button>
        </div>

        {/* Club Finder */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Users className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Clubs</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Find clubs matching your interests</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Browse Clubs
          </button>
        </div>

        {/* Marketplace */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <ShoppingBag className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Marketplace</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Buy and sell student items</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Visit Marketplace
          </button>
        </div>
      </div>
    </div>
  );
};

export default Social;
import React from 'react';
import { Wallet, GraduationCap, Tag } from 'lucide-react';

const Finance = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Finance & Budgeting</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Expense Tracker */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Wallet className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Expenses</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Track and manage your spending</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Track Expenses
          </button>
        </div>

        {/* Scholarships */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <GraduationCap className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Scholarships</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Find relevant scholarship opportunities</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            Find Scholarships
          </button>
        </div>

        {/* Student Discounts */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <div className="flex items-center mb-4">
            <Tag className="h-6 w-6 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Discounts</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">Discover student deals and offers</p>
          <button className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors">
            View Deals
          </button>
        </div>
      </div>
    </div>
  );
};

export default Finance;
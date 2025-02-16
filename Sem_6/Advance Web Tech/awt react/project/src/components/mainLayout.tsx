import React, { useState } from 'react';
import { Routes, Route, NavLink, useLocation } from 'react-router-dom';
import { 
  Bell, 
  BookOpen,
  Brain,
  Calendar,
  ChevronDown,
  ClipboardList,
  CreditCard,
  GraduationCap,
  Heart,
  Layout as LayoutIcon,
  LineChart,
  Menu,
  Moon,
  Search,
  Settings,
  Sun,
  Users,
  X
} from 'lucide-react';

// Import pages
import Dashboard from '../pages/Dashboard';
import Academics from '../pages/Academics';
import Productivity from '../pages/Productivity';
import Courses from '../pages/Courses';
import Performance from '../pages/Performance';
import Wellbeing from '../pages/Wellbeing';
import Career from '../pages/Career';
import Finance from '../pages/Finance';
import Social from '../pages/Social';

const Layout = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const [isSidebarOpen, setSidebarOpen] = useState(true);
  const location = useLocation();

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.documentElement.classList.toggle('dark');
  };

  const navigationItems = [
    { path: '/', name: 'Dashboard', icon: LayoutIcon },
    { path: '/academics', name: 'Academics & Learning', icon: BookOpen },
    { path: '/productivity', name: 'Productivity', icon: ClipboardList },
    { path: '/courses', name: 'Courses', icon: GraduationCap },
    { path: '/performance', name: 'Performance', icon: LineChart },
    { path: '/wellbeing', name: 'Well-being', icon: Heart },
    { path: '/career', name: 'Career', icon: Brain },
    { path: '/finance', name: 'Finance', icon: CreditCard },
    { path: '/social', name: 'Social', icon: Users }
  ];

  return (
    <div className={`min-h-screen ${darkMode ? 'dark' : ''}`}>
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
        {/* Top Navigation */}
        <nav className="fixed top-0 z-30 w-full bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
          <div className="px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <button
                  onClick={() => setSidebarOpen(!isSidebarOpen)}
                  className="p-2 rounded-md text-gray-500 hover:text-gray-900 dark:hover:text-white focus:outline-none"
                >
                  {isSidebarOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
                </button>
                <LayoutIcon className="h-8 w-8 text-indigo-600 dark:text-indigo-400 ml-2" />
                <span className="ml-2 text-xl font-bold text-gray-900 dark:text-white">StudyHub</span>
              </div>

              <div className="flex items-center space-x-4">
                {/* Search */}
                <div className="relative hidden md:block">
                  <input
                    type="text"
                    placeholder="Search..."
                    className="w-64 px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                  <Search className="absolute right-3 top-2.5 h-5 w-5 text-gray-400" />
                </div>

                {/* Notifications */}
                <button className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                  <Bell className="h-6 w-6 text-gray-500 dark:text-gray-400" />
                </button>

                {/* Dark Mode Toggle */}
                <button 
                  onClick={toggleDarkMode}
                  className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  {darkMode ? (
                    <Sun className="h-6 w-6 text-gray-500 dark:text-gray-400" />
                  ) : (
                    <Moon className="h-6 w-6 text-gray-500 dark:text-gray-400" />
                  )}
                </button>

                {/* Settings */}
                <button className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                  <Settings className="h-6 w-6 text-gray-500 dark:text-gray-400" />
                </button>

                {/* Profile */}
                <div className="relative">
                  <button
                    onClick={() => setIsProfileOpen(!isProfileOpen)}
                    className="flex items-center space-x-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700"
                  >
                    <img
                      src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      alt="Profile"
                      className="h-8 w-8 rounded-full"
                    />
                    <ChevronDown className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                  </button>

                  {isProfileOpen && (
                    <div className="absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5">
                      <div className="py-1">
                        <a href="#profile" className="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Your Profile</a>
                        <a href="#settings" className="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Settings</a>
                        <a href="#signout" className="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Sign out</a>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </nav>

        {/* Sidebar */}
        <aside className={`fixed left-0 z-20 w-64 h-full transition-transform duration-300 transform ${
          isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
        } bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700`}>
          <div className="h-16" /> {/* Spacer for navbar */}
          <nav className="mt-5 px-4">
            <div className="space-y-1">
              {navigationItems.map((item) => {
                const Icon = item.icon;
                return (
                  <NavLink
                    key={item.path}
                    to={item.path}
                    className={({ isActive }) =>
                      `flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-colors duration-150 ${
                        isActive
                          ? 'bg-indigo-50 dark:bg-indigo-900/50 text-indigo-600 dark:text-indigo-400'
                          : 'text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700'
                      }`
                    }
                  >
                    <Icon className="h-5 w-5 mr-3" />
                    {item.name}
                  </NavLink>
                );
              })}
            </div>
          </nav>
        </aside>

        {/* Main Content */}
        <div className={`transition-all duration-300 ${isSidebarOpen ? 'ml-64' : 'ml-0'}`}>
          <div className="h-16" /> {/* Spacer for navbar */}
          <main className="p-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/academics" element={<Academics />} />
              <Route path="/productivity" element={<Productivity />} />
              <Route path="/courses" element={<Courses />} />
              <Route path="/performance" element={<Performance />} />
              <Route path="/wellbeing" element={<Wellbeing />} />
              <Route path="/career" element={<Career />} />
              <Route path="/finance" element={<Finance />} />
              <Route path="/social" element={<Social />} />
            </Routes>
          </main>
        </div>
      </div>
    </div>
  );
};

export default Layout;
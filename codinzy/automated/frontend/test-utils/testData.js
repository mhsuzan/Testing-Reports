/**
 * @jest-environment jsdom
 */

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import userEvent from '@testing-library/user-event';

// Mock dependencies before imports
jest.mock('axios', () => ({
  create: jest.fn(() => ({
    get: jest.fn(),
    post: jest.fn(),
    put: jest.fn(),
    delete: jest.fn(),
    interceptors: {
      request: { use: jest.fn(), eject: jest.fn() },
      response: { use: jest.fn(), eject: jest.fn() },
    },
  })),
  get: jest.fn(),
  post: jest.fn(),
}));

jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
  useLocation: jest.fn(),
  useParams: jest.fn(),
  BrowserRouter: ({ children }) => <div>{children}</div>,
  Routes: ({ children }) => <div>{children}</div>,
  Route: ({ children }) => <div>{children}</div>,
}));

jest.mock('react-hot-toast', () => ({
  toast: {
    success: jest.fn(),
    error: jest.fn(),
    info: jest.fn(),
  },
}));

// Extend Jest timeout for async operations
jest.setTimeout(10000);

// Global test utilities
export const testHelpers = {
  /**
   * Wait for an element to appear in the DOM
   */
  waitForElement: async (selector) => {
    return waitFor(() => screen.getByTestId(selector), { timeout: 5000 });
  },

  /**
   * Check if element is in document
   */
  elementExists: (selector) => {
    const element = screen.queryByTestId(selector);
    return element !== null;
  },

  /**
   * Get input element and type text
   */
  typeInInput: async (name, text) => {
    const input = screen.getByRole('textbox', { name }) || 
                  screen.getByLabelText(name) ||
                  screen.getByPlaceholderText(name);
    await userEvent.clear(input);
    await userEvent.type(input, text);
    return input;
  },

  /**
   * Click a button by text
   */
  clickButton: async (text) => {
    const button = screen.getByRole('button', { name: text });
    await userEvent.click(button);
    return button;
  },

  /**
   * Select an option from dropdown
   */
  selectOption: async (label, optionText) => {
    const select = screen.getByRole('combobox', { name: label }) ||
                   screen.getByLabelText(label);
    await userEvent.selectOptions(select, optionText);
  },

  /**
   * Fill out a form
   */
  fillForm: async (formData) => {
    for (const [field, value] of Object.entries(formData)) {
      if (typeof value === 'boolean') {
        const checkbox = screen.getByRole('checkbox', { name: field });
        if (value) await userEvent.click(checkbox);
      } else if (value.includes('select')) {
        await testHelpers.selectOption(field, value.replace('select:', ''));
      } else {
        await testHelpers.typeInInput(field, value);
      }
    }
  },

  /**
   * Check API was called with specific data
   */
  expectApiCall: (mockFn, expectedCall = 0) => {
    expect(mockFn).toHaveBeenCalledTimes(expectedCall);
  },
};

/**
 * Mock API response helper
 */
export const mockApiResponse = (data, status = 200) => ({
  data,
  status,
  statusText: 'OK',
  headers: {},
  config: {},
});

/**
 * Mock API error
 */
export const mockApiError = (message = 'Request failed', status = 400) => {
  const error = new Error(message);
  error.response = {
    data: { detail: message },
    status,
    statusText: 'Error',
    headers: {},
    config: {},
  };
  return error;
};

/**
 * Create mock user data
 */
export const createMockUser = (overrides = {}) => ({
  id: 1,
  username: 'testuser',
  email: 'test@example.com',
  name: 'Test User',
  user_type: 'student',
  is_student: true,
  is_teacher: false,
  is_admin: false,
  ...overrides,
});

/**
 * Create mock student data
 */
export const createMockStudent = (overrides = {}) => ({
  id: 1,
  user: createMockUser(),
  name: 'Test Student',
  email: 'student@test.com',
  school_name: 'Test School',
  student_grade: '5',
  enrolled: true,
  account_status: 'active',
  ...overrides,
});

/**
 * Create mock course data
 */
export const createMockCourse = (overrides = {}) => ({
  id: 1,
  title: 'Python Basics',
  description: 'Learn Python programming',
  language: 'Python',
  difficulty_level: 'beginner',
  is_active: true,
  modules_count: 5,
  lessons_count: 20,
  ...overrides,
});

/**
 * Create mock scheduled class data
 */
export const createMockScheduledClass = (overrides = {}) => ({
  id: 1,
  title: 'Python Lesson 1',
  course: createMockCourse(),
  teacher: {
    id: 1,
    name: 'Test Teacher',
    email: 'teacher@test.com',
  },
  students: [createMockStudent()],
  scheduled_start_time: new Date().toISOString(),
  scheduled_end_time: new Date(Date.now() + 3600000).toISOString(),
  status: 'scheduled',
  class_method: 'jitsi',
  ...overrides,
});

/**
 * Create mock payment data
 */
export const createMockPayment = (overrides = {}) => ({
  id: 1,
  student: createMockStudent(),
  course: createMockCourse(),
  amount: 100.00,
  status: 'pending',
  payment_method: 'stripe',
  currency: 'USD',
  ...overrides,
});

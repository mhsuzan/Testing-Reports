# Manual Testing Checklist - Codinzy Platform

## 1. Authentication Module

### 1.1 User Registration
- [ ] Verify registration form fields validation
- [ ] Test email format validation
- [ ] Test password strength requirements
- [ ] Test duplicate username prevention
- [ ] Test duplicate email prevention
- [ ] Test successful registration flow
- [ ] Test redirect after registration
- [ ] Test email verification link

### 1.2 User Login
- [ ] Test valid login credentials
- [ ] Test invalid password
- [ ] Test non-existent username
- [ ] Test empty fields validation
- [ ] Test "Remember Me" functionality
- [ ] Test session persistence
- [ ] Test login with different user types (student, teacher, admin)

### 1.3 Password Reset
- [ ] Test password reset request with valid email
- [ ] Test password reset request with invalid email
- [ ] Test password reset link expiration
- [ ] Test new password validation
- [ ] Test successful password change

### 1.4 Logout
- [ ] Test logout functionality
- [ ] Test session cleanup after logout
- [ ] Test redirect to login page

---

## 2. Student Dashboard

### 2.1 Dashboard Overview
- [ ] Test dashboard loads correctly
- [ ] Test upcoming classes display
- [ ] Test enrolled courses display
- [ ] Test progress indicators
- [ ] Test recent achievements

### 2.2 My Courses
- [ ] Test course list display
- [ ] Test course card information
- [ ] Test course progress tracking
- [ ] Test continue learning button
- [ ] Test course search/filter

### 2.3 My Lessons
- [ ] Test lesson list display
- [ ] Test lesson completion status
- [ ] Test lesson navigation
- [ ] Test video player functionality
- [ ] Test quiz access

### 2.4 My Projects
- [ ] Test projects list display
- [ ] Test project submission upload
- [ ] Test project status tracking
- [ ] Test project feedback display

### 2.5 Certificates
- [ ] Test certificate list
- [ ] Test certificate download
- [ ] Test certificate verification

---

## 3. Teacher Dashboard

### 3.1 Dashboard Overview
- [ ] Test dashboard loads correctly
- [ ] Test scheduled classes display
- [ ] Test student progress overview
- [ ] Test upcoming classes list

### 3.2 Teacher Calendar
- [ ] Test calendar view loads
- [ ] Test class scheduling
- [ ] Test class rescheduling
- [ ] Test availability management
- [ ] Test class cancellation
- [ ] Test calendar sync

### 3.3 Student Management
- [ ] Test student list display
- [ ] Test student progress tracking
- [ ] Test student performance metrics
- [ ] Test student feedback submission

### 3.4 Class Management
- [ ] Test class creation
- [ ] Test class editing
- [ ] Test class materials upload
- [ ] Test activity creation

---

## 4. Classroom

### 4.1 Jitsi Integration
- [ ] Test room joining
- [ ] Test video/audio toggle
- [ ] Test screen sharing
- [ ] Test chat functionality
- [ ] Test participant list
- [ ] Test recording controls
- [ ] Test whiteboard access

### 4.2 Whereby Integration
- [ ] Test room joining
- [ ] Test video/audio toggle
- [ ] Test breakout rooms
- [ ] Test whiteboard functionality

### 4.3 Class Activities
- [ ] Test activity list display
- [ ] Test activity submission
- [ ] Test quiz functionality
- [ ] Test code editor integration
- [ ] Test activity grading

### 4.4 Student Submissions
- [ ] Test submission upload
- [ ] Test submission review
- [ ] Test feedback submission
- [ ] Test grade assignment

---

## 5. Payments & Billing

### 5.1 Payment Processing
- [ ] Test payment page loading
- [ ] Test card validation
- [ ] Test successful payment
- [ ] Test payment failure handling
- [ ] Test payment confirmation

### 5.2 Discount Codes
- [ ] Test valid discount code
- [ ] Test invalid discount code
- [ ] Test expired discount code
- [ ] Test discount calculation

### 5.3 Billing History
- [ ] Test transaction list
- [ ] Test invoice download
- [ ] Test payment status display

### 5.4 Auto-charge
- [ ] Test auto-charge enable/disable
- [ ] Test automatic payment processing
- [ ] Test auto-charge notification

---

## 6. Lead Management

### 6.1 Lead Creation
- [ ] Test lead form validation
- [ ] Test lead creation from trial booking
- [ ] Test lead import
- [ ] Test lead assignment

### 6.2 Lead Tracking
- [ ] Test lead list display
- [ ] Test lead stage progression
- [ ] Test lead activity logging
- [ ] Test lead notes

### 6.3 Trial Class Booking
- [ ] Test slot selection
- [ ] Test confirmation email
- [ ] Test calendar invite
- [ ] Test reminder notifications

### 6.4 Follow-up
- [ ] Test follow-up scheduling
- [ ] Test communication history
- [ ] Test conversion tracking

---

## 7. Gamification

### 7.1 Badges
- [ ] Test badge display
- [ ] Test badge earning criteria
- [ ] Test badge notification
- [ ] Test badge sharing

### 7.2 XP System
- [ ] Test XP accumulation
- [ ] Test XP display
- [ ] Test XP milestones
- [ ] Test XP rewards

### 7.3 Leaderboard
- [ ] Test leaderboard display
- [ ] Test ranking calculation
- [ ] Test period filtering
- [ ] Test user position

---

## 8. UI/UX Testing

### 8.1 Navigation
- [ ] Test main navigation
- [ ] Test sidebar menu
- [ ] Test breadcrumbs
- [ ] Test back button functionality

### 8.2 Responsive Design
- [ ] Test desktop layout (1920px)
- [ ] Test laptop layout (1366px)
- [ ] Test tablet layout (768px)
- [ ] Test mobile layout (375px)

### 8.3 Accessibility
- [ ] Test keyboard navigation
- [ ] Test screen reader compatibility
- [ ] Test color contrast
- [ ] Test focus indicators
- [ ] Test ARIA labels

### 8.4 Performance
- [ ] Test page load time (< 3s)
- [ ] Test API response time (< 500ms)
- [ ] Test image optimization
- [ ] Test lazy loading

---

## 9. Security Testing

### 9.1 Authentication
- [ ] Test session timeout
- [ ] Test concurrent session handling
- [ ] Test secure password storage
- [ ] Test token validation

### 9.2 Authorization
- [ ] Test role-based access
- [ ] Test permission checks
- [ ] Test URL manipulation
- [ ] Test IDOR prevention

### 9.3 Data Validation
- [ ] Test SQL injection prevention
- [ ] Test XSS prevention
- [ ] Test CSRF protection
- [ ] Test file upload validation

---

## 10. Cross-Browser Testing

### 10.1 Chrome
- [ ] Test latest Chrome version
- [ ] Test Chrome on Windows
- [ ] Test Chrome on macOS
- [ ] Test Chrome on Linux

### 10.2 Firefox
- [ ] Test latest Firefox version
- [ ] Test Firefox on Windows
- [ ] Test Firefox on macOS
- [ ] Test Firefox on Linux

### 10.3 Safari
- [ ] Test latest Safari version
- [ ] Test Safari on macOS
- [ ] Test Safari on iOS

### 10.4 Edge
- [ ] Test latest Edge version
- [ ] Test Edge on Windows

---

## 11. Integration Testing

### 11.1 Email Integration
- [ ] Test welcome email
- [ ] Test class reminder email
- [ ] Test payment confirmation email
- [ ] Test certificate email

### 11.2 WhatsApp Integration
- [ ] Test message delivery
- [ ] Test template messages
- [ ] Test notification triggers

### 11.3 Calendar Integration
- [ ] Test .ics file generation
- [ ] Test Google Calendar sync
- [ ] Test Outlook Calendar sync

### 11.4 Video Integration
- [ ] Test Jitsi room creation
- [ ] Test Whereby room creation
- [ ] Test recording storage

---

## 12. Database Testing

### 12.1 Data Integrity
- [ ] Test foreign key constraints
- [ ] Test unique constraints
- [ ] Test cascade delete
- [ ] Test data validation

### 12.2 Performance
- [ ] Test query optimization
- [ ] Test index efficiency
- [ ] Test large dataset handling
- [ ] Test concurrent transactions

---

## Testing Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| QA Lead | | | |
| Test Engineer | | | |
| Dev Lead | | | |
| Product Owner | | | |

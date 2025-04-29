describe('Product Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

describe('Dashboard Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should navigate to dashboard from product details', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')

    // Click the dashboard button
    cy.get('[data-testid="dashboard-button"]').click()

    // Verify we're on the dashboard page
    cy.url().should('eq', Cypress.config().baseUrl + '/')
    
    // Verify dashboard is displayed
    cy.contains('Supply Chain Dashboard').should('be.visible')
  })
})

  it('should navigate to product details when clicking a product', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')
  })

describe('Dashboard Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should navigate to dashboard from product details', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')

    // Click the dashboard button
    cy.get('[data-testid="dashboard-button"]').click()

    // Verify we're on the dashboard page
    cy.url().should('eq', Cypress.config().baseUrl + '/')
    
    // Verify dashboard is displayed
    cy.contains('Supply Chain Dashboard').should('be.visible')
  })
})
})

describe('Dashboard Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should navigate to dashboard from product details', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')

    // Click the dashboard button
    cy.get('[data-testid="dashboard-button"]').click()

    // Verify we're on the dashboard page
    cy.url().should('eq', Cypress.config().baseUrl + '/')
    
    // Verify dashboard is displayed
    cy.contains('Supply Chain Dashboard').should('be.visible')
  })
}) 
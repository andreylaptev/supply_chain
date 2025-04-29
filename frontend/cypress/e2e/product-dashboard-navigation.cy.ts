describe('Product Dashboard Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should navigate to product details and then to dashboard', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')

    // Click the dashboard button
    cy.get('[data-testid="dashboard-button"]').click()

    // Verify we're on the dashboard page
    cy.contains('Supply Chain Dashboard').should('be.visible')
  })
})
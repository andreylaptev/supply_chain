describe('Product Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should navigate to product details when clicking a product', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Verify product details are displayed
    cy.get('[data-testid="product-details"]').should('be.visible')
  })

  it('should navigate to the Supply Chain Dashboard from product details', () => {
    // Click the first product in the list
    cy.get('[data-testid="product-item"]').first().click()
    
    // Verify we're on the product details page
    cy.url().should('include', '/product/')
    
    // Click the Dashboard button
    cy.get('[data-testid="HomeIcon"]').click()
    
    // Verify we're on the Supply Chain Dashboard
    cy.url().should('include', '/');
    cy.get('h6').contains('Supply Chain Dashboard').should('be.visible');
  })
}) 
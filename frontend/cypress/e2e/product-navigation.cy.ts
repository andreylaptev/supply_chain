describe('Product Navigation', () => {
  it('should navigate to product details and back to dashboard', () => {
    // Step 1: Go to the landing page
    cy.visit('/');

    // Step 2: Click any product
    cy.get('[data-testid="product-card"]').first().click();

    // Step 3: Assert that the product screen is open
    cy.url().should('include', '/product/');
    cy.get('[data-testid="product-details"]').should('be.visible');

    // Step 4: Click "dashboard" button
    cy.get('[data-testid="dashboard-button"]').click();

    // Step 5: Assert that the "Supply Chain Dashboard" screen is open
    cy.url().should('eq', Cypress.config().baseUrl + '/');
    cy.get('[data-testid="dashboard-screen"]').should('be.visible');
  });
});
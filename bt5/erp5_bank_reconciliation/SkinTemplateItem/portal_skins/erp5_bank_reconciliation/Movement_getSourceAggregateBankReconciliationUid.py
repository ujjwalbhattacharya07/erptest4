for bank_reconciliation in context.getAggregateValueList(portal_type='Bank Reconciliation'):
  if bank_reconciliation.getSourcePayment() == context.getSourcePayment():
    return bank_reconciliation.getUid()

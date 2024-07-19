import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = this._validateNumber(amount, 'Amount must be a number');
    this._currency = this._validateCurrency(currency, 'Currency must be an instance of Currency');
  }

  _validateNumber(value, errorMessage) {
    if (typeof value !== 'number') {
      throw new TypeError(errorMessage);
    }
    return value;
  }

  _validateCurrency(value, errorMessage) {
    if (!(value instanceof Currency)) {
      throw new TypeError(errorMessage);
    }
    return value;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = this._validateNumber(value, 'Amount must be a number');
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = this._validateCurrency(value, 'Currency must be an instance of Currency');
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

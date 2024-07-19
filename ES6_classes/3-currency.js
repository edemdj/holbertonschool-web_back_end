export default class Currency {
    constructor(code, name) {
      this._code = this._validateString(code, 'Code must be a string');
      this._name = this._validateString(name, 'Name must be a string');
    }
  
    _validateString(value, errorMessage) {
      if (typeof value !== 'string') {
        throw new TypeError(errorMessage);
      }
      return value;
    }
  
    get code() {
      return this._code;
    }
  
    set code(value) {
      this._code = this._validateString(value, 'Code must be a string');
    }
  
    get name() {
      return this._name;
    }
  
    set name(value) {
      this._name = this._validateString(value, 'Name must be a string');
    }
  
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }
  
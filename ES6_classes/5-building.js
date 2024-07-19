export default class Building {
    constructor(sqft) {
      this._sqft = this._validateNumber(sqft, 'Sqft must be a number');
      if (new.target === Building) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    _validateNumber(value, errorMessage) {
      if (typeof value !== 'number') {
        throw new TypeError(errorMessage);
      }
      return value;
    }
  
    get sqft() {
      return this._sqft;
    }
  

    evacuationWarningMessage() {
      Error('Cannot instantiate abstract class Building directly');
    }
  }
  
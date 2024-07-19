export default class HolbertonCourse {
    constructor(name, length, students) {
      this._name = this._validateString(name, 'Name must be a string');
      this._length = this._validateNumber(length, 'Length must be a number');
      this._students = this._validateStudents(students, 'Students must be an array of strings');
    }
  
    _validateString(value, errorMessage) {
      if (typeof value !== 'string') {
        throw new TypeError(errorMessage);
      }
      return value;
    }
  
    _validateNumber(value, errorMessage) {
      if (typeof value !== 'number') {
        throw new TypeError(errorMessage);
      }
      return value;
    }
  
    _validateStudents(value, errorMessage) {
      if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
        throw new TypeError(errorMessage);
      }
      return value;
    }
  
    get name() {
      return this._name;
    }
  
    set name(value) {
      this._name = this._validateString(value, 'Name must be a string');
    }
  
    get length() {
      return this._length;
    }
  
    set length(value) {
      this._length = this._validateNumber(value, 'Length must be a number');
    }
  
    get students() {
      return this._students;
    }
  
    set students(value) {
      this._students = this._validateStudents(value, 'Students must be an array of strings');
    }
  }
  
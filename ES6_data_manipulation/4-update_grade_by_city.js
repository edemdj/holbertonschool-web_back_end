function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);

  return filteredStudents.map((student) => {
    const gradeEntry = newGrades.find((grade) => grade.studentId === student.id);
    return {
      ...student,
      grade: gradeEntry ? gradeEntry.grade : 'N/A',
    };
  });
}

export default updateStudentGradeByCity;

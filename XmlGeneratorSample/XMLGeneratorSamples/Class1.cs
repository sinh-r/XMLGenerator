namespace XMLGeneratorSamples
{
    public class Class1
    {
        public int ID { get; set; }
        public string Name { get; set; }
    }

    public class Student
    {
        public Guid Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int Age { get; set; }
    }

    public static class Student1
    {
        public static Guid Id { get; set; }
        public static string FirstName { get; set; }
        public static string LastName { get; set; }
        public static int Age { get; set; }
    }
}
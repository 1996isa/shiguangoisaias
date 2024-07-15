using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int numDisks = 3; // Número de discos
        Stack<int> source = new Stack<int>(numDisks);
        Stack<int> auxiliary = new Stack<int>(numDisks);
        Stack<int> target = new Stack<int>(numDisks);

        // Inicializar la torre fuente con discos
        for (int i = numDisks; i >= 1; i--)
        {
            source.Push(i);
        }

        SolveHanoi(numDisks, source, target, auxiliary);

        Console.WriteLine("Discos en la torre objetivo:");
        foreach (var disk in target)
        {
            Console.WriteLine(disk);
        }
    }

    static void SolveHanoi(int n, Stack<int> source, Stack<int> target, Stack<int> auxiliary)
    {
        if (n > 0)
        {
            SolveHanoi(n - 1, source, auxiliary, target);
            MoveDisk(source, target);
            SolveHanoi(n - 1, auxiliary, target, source);
        }
    }

    static void MoveDisk(Stack<int> source, Stack<int> target)
    {
        int disk = source.Pop();
        target.Push(disk);
        Console.WriteLine($"Moviendo disco {disk} desde torre {GetName(source)} a torre {GetName(target)}");
    }

    static string GetName(Stack<int> stack)
    {
        if (stack.Count == 0)
        {
            return "S/A/T";
        }
        int hashCode = stack.GetHashCode();
        return hashCode.ToString();
    }
}

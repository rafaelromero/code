using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Xml;
using System.Configuration;
using System.Collections.Specialized;

//little console program that changes database connection strings for multiple or single projects. 

namespace hamster
{
   public class Program
    {
       public static int Main(string[] args)
        {
            Tricks tricks =new Tricks();

            if (args.Length == 0)
            {
                System.Console.WriteLine("help\n");
                System.Console.WriteLine("-d  [project dev directory | Project directory]");
                System.Console.WriteLine("-fx [fix project base connections (framework, home, security)] ");
                System.Console.WriteLine("-fxs[fix single project]");
                System.Console.WriteLine("-c  [connection string]");
                System.Console.WriteLine("");
                System.Console.WriteLine("!sample command yall! " );
                System.Console.WriteLine("hamster -d C:\\mydev_folder\\Dev\\ -fx   -c  \"data source=SOMESERVERNAME\\SOMEINSTANCENAME;initial catalog=DBNAME; User ID=DBUSER; Password=DBPASSWORD;\"");

                return 1;
               
            }

            if (args.Length < 5 || args.Length > 5)
            {
                System.Console.WriteLine("wrong command: too few or too many arguments");

                foreach (string sf in args)
                {
                    System.Console.WriteLine("item:" + sf);

                }
                return 1;
            }

            string option_directory             = args[0].Trim();
            string directory                    = args[1].Trim();
            string option_fix                   = args[2].Trim();
            string option_connectionstring      = args[3].Trim();
            string connectionString             = args[4].Trim();

            List<string> fixOptionList = new List<string>(){"-fx", "-fxs"};


            if (option_directory != "-d")
            {
                System.Console.WriteLine("wrong command: directory option missing");
                return 1;
            }
            if (fixOptionList.Contains(option_fix) == false)
            {
                System.Console.WriteLine("wrong command : fix option missing");
                System.Console.WriteLine(option_fix);
                return 1;
            }

            if (option_connectionstring != "-c")
            {
                System.Console.WriteLine("wrong command : connection option missing");
                return 1;
            }



            if (option_fix == "-fx")
            {
                tricks.SpinAllWheels(directory, connectionString);
            }
                
            if (option_fix == "-fxs")
            {
                tricks.SpinSingleWheel(directory, connectionString);
            }


            System.Console.WriteLine("Happy Hamster! :p");


            return 0;
        }

   }

public class Tricks{


    
       public int SpinAllWheels(string directory, string connectionString){

           int result = 0;

           result = fixconfig(directory + @"\path\to\project",       connectionString);
           result = fixconfig(directory + @"\path\to\project",         connectionString);
           result = fixconfig(directory + @"\path\to\project", connectionString);

           return result;
       }

       public int SpinSingleWheel(string directory, string connectionString)
       {
           int result = 0;
           result = fixconfig(directory, connectionString);

           return result;
       }


        public static int fixconfig(string directory, string connectionString){

            string foundConnectionString = string.Empty;
            string file = directory + "\\Web.config";
            XmlDocument xdoc = new XmlDocument();
            xdoc.Load(file);
            XmlNodeList xnodes = xdoc.SelectNodes("/configuration/appSettings/add[contains(@key,'ConnectString')]");

            foreach (XmlNode xn in xnodes)
            {
                string val;
                if (xn.Attributes != null)
                {
                    val = xn.Attributes[1].Value.ToString();

                    if (val.Contains("data source"))
                    {
                        foundConnectionString = val;
                        xn.Attributes[1].Value = connectionString;
                    }

                   

                   

                }



            }


            xdoc.Save(file);

            return 1;
        }

}


    
}

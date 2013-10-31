<?php
mysql_connect("localhost","root","$YOUR_PASSWORD");
mysql_select_db("$DATABASE_NAME");

if (isset($_POST['search_query'])) {
$search_query = mysql_real_escape_string(htmlentities($_POST['search_query']));
echo "<div class=\"searchText\">Search</div>";

//explode the search term
$search_query_x = explode(" ",$search_query);

foreach($search_query_x as $search_each) {
$x++;
if($x==1)
$construct .="keywords LIKE '%$search_each%'";
else
$construct .="AND keywords LIKE '%$search_each%'";
}
$construct ="SELECT * FROM search WHERE $construct";
$run = mysql_query($construct);

$foundnum = mysql_num_rows($run);
if ($foundnum==0) {
echo "It probably exists somewhere on the meshnet, but I cant find it. Sorry bro!";
} else
{
echo "<p>$foundnum results</p>";
while($runrows = mysql_fetch_assoc($run))
{
$title = $runrows ['title'];
$desc = $runrows ['description'];
$url = $runrows ['url'];
echo "
<div class='width: 400px;'>
<div class='title'><a href='$url'><b>$title</b></a></div>
<div class='url'>$url</div>
<div class='desc'>$desc</div>
</div>
<br />
";
}
}
}
else
{
echo "An ERROR HAS OCCURED ...";	
}
?>